// All content is ordinary HTML. JavaScript only enhances image enlargement.
(() => {
  const dialog = document.querySelector('#image-viewer');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const image = dialog.querySelector('.viewer-body > img');
  const caption = dialog.querySelector('.viewer-caption');
  let group = [], index = 0, opener;
  function render() {
    const anchor = group[index];
    image.src = anchor.href;
    image.alt = anchor.querySelector('img').alt;
    caption.replaceChildren(anchor.closest('figure').querySelector('figcaption').cloneNode(true));
  }
  document.querySelectorAll('[data-lightbox]').forEach(anchor => {
    anchor.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = anchor;
      group = [...anchor.closest('.gallery-grid').querySelectorAll('[data-lightbox]')];
      index = group.indexOf(anchor);
      render();
      dialog.showModal();
      document.body.style.overflow = 'hidden';
    });
  });
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  function step(delta) { index = (index + delta + group.length) % group.length; render(); }
  dialog.querySelector('[data-prev]').addEventListener('click', () => step(-1));
  dialog.querySelector('[data-next]').addEventListener('click', () => step(1));
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowRight') { event.preventDefault(); step(1); }
    if (event.key === 'ArrowLeft') { event.preventDefault(); step(-1); }
  });
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => { document.body.style.overflow = ''; opener?.focus(); });
})();
