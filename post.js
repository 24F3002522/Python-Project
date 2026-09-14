async function renderPost() {
    const headerEl = document.getElementById('post-header');
    const bodyEl = document.getElementById('post-body');
    const footerNavEl = document.getElementById('post-footer-nav');
  
    const params = new URLSearchParams(window.location.search);
    const collection = params.get('collection') === 'letters' ? 'letters' : 'poems';
    const slug = params.get('slug');
    const backHref = `${window.SITE_ROOT}pages/${collection}.html`;
    const backLabel = collection === 'poems' ? 'Poems' : 'Letters';
    const backLink = `<a class="back-link" href="${backHref}">&larr; Back to ${backLabel}</a>`;
  
    if (!slug) {
      headerEl.innerHTML = `${backLink}<p class="empty-note">No piece was specified.</p>`;
      return;
    }
  
    try {
      const post = await loadPost(collection, `${slug}.md`);
      document.title = `${post.title} — Dave`;
  
      headerEl.innerHTML = `
        ${backLink}
        <h1>${escapeHtml(post.title)}</h1>
        <p class="post-date">${formatDate(post.date)}</p>
      `;
  
      const typeClass = collection === 'poems' ? 'type-poem' : 'type-letter';
      bodyEl.classList.add(typeClass);
      bodyEl.innerHTML =
        collection === 'poems' ? renderPoemBody(post.content) : renderLetterBody(post.content);
  
      footerNavEl.innerHTML = backLink;
    } catch (err) {
      console.error(err);
      headerEl.innerHTML = `${backLink}<p class="empty-note">This piece couldn\u2019t be found.</p>`;
    }
  }
  
  document.addEventListener('DOMContentLoaded', renderPost);