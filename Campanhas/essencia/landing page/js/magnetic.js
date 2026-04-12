/* ── Efeito magnético nos botões ── */

const isTouchDevice = 'ontouchstart' in window;

if (!isTouchDevice) {
  document.querySelectorAll('.magnetic').forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = (e.clientX - rect.left - rect.width  / 2) * 0.28;
      const y = (e.clientY - rect.top  - rect.height / 2) * 0.28;
      el.style.transform = `translate(${x}px, ${y}px)`;
    });

    el.addEventListener('mouseleave', () => {
      el.style.transform = 'translate(0, 0)';
      el.style.transition = 'transform 0.4s ease';
    });

    el.addEventListener('mouseenter', () => {
      el.style.transition = 'transform 0.1s ease';
    });
  });
}
