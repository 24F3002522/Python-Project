/**
 * Loads the shared header and footer into every page.
 *
 * Every page defines `window.SITE_ROOT` before this script runs —
 * "" for index.html at the project root, "../" for anything one
 * folder deep (everything in /pages/). Component HTML files use the
 * literal token {{ROOT}} in place of that prefix so the same header
 * and footer file works from any folder depth.
 */

async function loadComponent(targetId, fileName) {
  const target = document.getElementById(targetId);
  if (!target) return;

  try {
    const res = await fetch(`${window.SITE_ROOT}components/${fileName}`);
    if (!res.ok) throw new Error(`Could not load ${fileName}`);
    const raw = await res.text();
    target.innerHTML = raw.replaceAll('{{ROOT}}', window.SITE_ROOT);
  } catch (err) {
    console.error(err);
  }
}

function markActiveNavLink() {
  const current = document.body.dataset.page;
  if (!current) return;
  document.querySelectorAll('.site-nav a[data-nav]').forEach((link) => {
    if (link.dataset.nav === current) {
      link.classList.add('active');
    }
  });
}

function fillCopyrightYear() {
  const el = document.getElementById('year');
  if (el) el.textContent = new Date().getFullYear();
}

document.addEventListener('DOMContentLoaded', async () => {
  await loadComponent('header-placeholder', 'header.html');
  await loadComponent('footer-placeholder', 'footer.html');
  markActiveNavLink();
  fillCopyrightYear();
});