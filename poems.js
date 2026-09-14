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
  
  document.addEventListener('DOMContentLoaded', () => {
    renderListing('poems', 'poems-list', 'No poems published yet — add one to posts/poems/.');
  });