/**
 * Shared content layer.
 *
 * Poems and letters live as plain .md files with a small frontmatter
 * block, e.g.:
 *
 *   ---
 *   title: The Quiet Hour
 *   date: 2026-01-15
 *   excerpt: A short line describing the piece.
 *   ---
 *
 *   Poem or letter text starts here.
 *
 * This is intentionally NOT full CommonMark — poems need every line
 * break preserved exactly as written, which standard Markdown does
 * not do. Supported syntax: the frontmatter block above, blank lines
 * as paragraph/stanza breaks, single line breaks preserved within a
 * stanza, and *italic* / **bold** for light emphasis.
 *
 * Each collection (poems, letters) has one manifest.json listing the
 * filenames in that folder. To add a new piece: drop a new .md file
 * into posts/<collection>/ and add its filename to that folder's
 * manifest.json.
 */

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function applyEmphasis(escapedLine) {
  return escapedLine
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>');
}

function parseFrontmatter(raw) {
  const match = raw.match(/^---\s*\n([\s\S]*?)\n---\s*\n?([\s\S]*)$/);
  if (!match) return { data: {}, content: raw.trim() };

  const [, block, content] = match;
  const data = {};

  block.split('\n').forEach((line) => {
    const idx = line.indexOf(':');
    if (idx === -1) return;
    const key = line.slice(0, idx).trim();
    let value = line.slice(idx + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    data[key] = value;
  });

  return { data, content: content.trim() };
}

// Poems: every line break matters. Blank lines separate stanzas.
function renderPoemBody(content) {
  return content
    .split(/\n\s*\n/)
    .map((stanza) => {
      const lines = stanza
        .split('\n')
        .map((line) => applyEmphasis(escapeHtml(line.trim())));
      return `<p class="stanza">${lines.join('<br>')}</p>`;
    })
    .join('');
}

// Letters: ordinary prose. Blank lines start a new paragraph; single
// line breaks inside a paragraph are treated as soft wraps.
function renderLetterBody(content) {
  return content
    .split(/\n\s*\n/)
    .map((para) => {
      const joined = para
        .split('\n')
        .map((line) => line.trim())
        .join(' ');
      return `<p>${applyEmphasis(escapeHtml(joined))}</p>`;
    })
    .join('');
}

function formatDate(dateStr) {
  const d = new Date(`${dateStr}T00:00:00`);
  if (Number.isNaN(d.getTime())) return dateStr;
  return d.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

async function loadManifest(collection) {
  const res = await fetch(`${window.SITE_ROOT}posts/${collection}/manifest.json`);
  if (!res.ok) throw new Error(`Could not load manifest for ${collection}`);
  return res.json();
}

async function loadPostRaw(collection, fileName) {
  const res = await fetch(`${window.SITE_ROOT}posts/${collection}/${fileName}`);
  if (!res.ok) throw new Error(`Could not load ${collection}/${fileName}`);
  return res.text();
}

async function loadPost(collection, fileName) {
  const raw = await loadPostRaw(collection, fileName);
  const { data, content } = parseFrontmatter(raw);
  const slug = fileName.replace(/\.md$/, '');
  return {
    slug,
    collection,
    title: data.title || slug,
    date: data.date || '',
    excerpt: data.excerpt || '',
    content,
  };
}

async function loadAllPosts(collection) {
  const files = await loadManifest(collection);
  const posts = await Promise.all(files.map((f) => loadPost(collection, f)));
  return posts.sort((a, b) => (a.date < b.date ? 1 : -1));
}

function postHref(post) {
  return `${window.SITE_ROOT}pages/post.html?collection=${post.collection}&slug=${encodeURIComponent(post.slug)}`;
}

function postRowHtml(post) {
  const kindClass = post.collection === 'poems' ? 'is-poem' : 'is-letter';
  return `
    <li class="post-row ${kindClass}">
      <a href="${postHref(post)}">
        <span class="post-row-main">
          <span class="kind-mark" aria-hidden="true"></span>
          <h3>${escapeHtml(post.title)}</h3>
        </span>
        <span class="excerpt">${escapeHtml(post.excerpt)}</span>
        <span class="post-date">${formatDate(post.date)}</span>
      </a>
    </li>
  `;
}

// Shared by pages/poems.html and pages/letters.html — renders a full,
// date-sorted listing for one collection into the given <ul>.
async function renderListing(collection, listId, emptyMessage) {
  const list = document.getElementById(listId);
  if (!list) return;

  try {
    const posts = await loadAllPosts(collection);
    if (posts.length === 0) {
      list.outerHTML = `<p class="empty-note">${emptyMessage}</p>`;
      return;
    }
    list.innerHTML = posts.map(postRowHtml).join('');
  } catch (err) {
    console.error(err);
    list.outerHTML = '<p class="empty-note">These couldn\'t be loaded right now.</p>';
  }
}