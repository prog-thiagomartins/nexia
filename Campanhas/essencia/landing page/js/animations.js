/* ── Anime.js: Fade-in on scroll ── */

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;

    anime({
      targets: entry.target,
      opacity: [0, 1],
      translateY: [24, 0],
      duration: 750,
      easing: 'easeOutExpo',
    });

    observer.unobserve(entry.target);
  });
}, { threshold: 0.12 });

document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));
