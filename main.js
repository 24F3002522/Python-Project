async function renderRecentWriting() {
    const list = document.getElementById('recent-list');
    if (!list) return;
  
    try {
      const [poems, letters] = await Promise.all([
        loadAllPosts('poems'),
        loadAllPosts('letters'),
      ]);
  
      const combined = [...poems, ...letters]
        .sort((a, b) => (a.date < b.date ? 1 : -1))
        .slice(0, 5);
  
      if (combined.length === 0) {
        list.outerHTML = '<p class="empty-note">Nothing published yet — add a poem or letter to get started.</p>';
        return;
      }
  
      list.innerHTML = combined.map(postRowHtml).join('');
    } catch (err) {
      console.error(err);
      list.outerHTML = '<p class="empty-note">Writing could not be loaded right now.</p>';
    }
  }
  
  document.addEventListener('DOMContentLoaded', renderRecentWriting);
  