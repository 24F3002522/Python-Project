def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b


a = bool(int(input("Enter first input (0/1): ")))
b = bool(int(input("Enter second input (0/1): ")))

print("AND :", int(AND(a, b)))
print("OR  :", int(OR(a, b)))
print("NOT A:", int(NOT(a)))
print("NAND:", int(NAND(a, b)))
print("NOR :", int(NOR(a, b)))
print("XOR :", int(XOR(a, b)))