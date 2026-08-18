        return remove_dups(found_vars)

    def visit_callable_type(self, t: CallableType) -> Type:
        found_vars = self.collect_vars(t)
        self.bound_tvars |= set(found_vars)
        result = super().visit_callable_type(t)
        self.bound_tvars -= set(found_vars)

        assert isinstance(result, ProperType) and isinstance(result, CallableType)
        result.variables = result.variables + tuple(found_vars)
        return result

    def visit_type_var(self, t: TypeVarType) -> Type:
        if t in self.poly_tvars and t not in self.bound_tvars:
            raise PolyTranslationError()
        return super().visit_type_var(t)

    def visit_param_spec(self, t: ParamSpecType) -> Type:
        if t in self.poly_tvars and t not in self.bound_tvars:
            raise PolyTranslationError()
        return super().visit_param_spec(t)

    def visit_type_var_tuple(self, t: TypeVarTupleType) -> Type:
        if t in self.poly_tvars and t not in self.bound_tvars:
            raise PolyTranslationError()
        return super().visit_type_var_tuple(t)

    def visit_type_alias_type(self, t: TypeAliasType) -> Type:
        if not t.args:
            return t.copy_modified()
        if not t.is_recursive:
            return get_proper_type(t).accept(self)
        # We can't handle polymorphic application for recursive generic aliases
        # without risking an infinite recursion, just give up for now.
        raise PolyTranslationError()

    def visit_instance(self, t: Instance) -> Type:
        if t.type.has_param_spec_type:
            # We need this special-casing to preserve the possibility to store a
            # generic function in an instance type. Things like
            #     forall T . Foo[[x: T], T]
            # are not really expressible in current type system, but this looks like
            # a useful feature, so let's keep it.
            param_spec_index = next(
                i for (i, tv) in enumerate(t.type.defn.type_vars) if isinstance(tv, ParamSpecType)
            )
            p = get_proper_type(t.args[param_spec_index])
            if isinstance(p, Parameters):
                found_vars = self.collect_vars(p)
                self.bound_tvars |= set(found_vars)
                new_args = [a.accept(self) for a in t.args]
                self.bound_tvars -= set(found_vars)

                repl = new_args[param_spec_index]
                assert isinstance(repl, ProperType) and isinstance(repl, Parameters)
                repl.variables = list(repl.variables) + list(found_vars)
                return t.copy_modified(args=new_args)
        # There is the same problem with callback protocols as with aliases
        # (callback protocols are essentially more flexible aliases to callables).
        if t.args and t.type.is_protocol and t.type.protocol_members == ["__call__"]:
            if t.type in self.seen_aliases:
                raise PolyTranslationError()
            call = mypy.subtypes.find_member("__call__", t, t, is_operator=True)
            assert call is not None
            return call.accept(
                PolyTranslator(self.poly_tvars, self.bound_tvars, self.seen_aliases | {t.type})
            )
        return super().visit_instance(t)