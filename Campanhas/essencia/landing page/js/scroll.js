/* ── GSAP: Horizontal scroll das fases ── */

gsap.registerPlugin(ScrollTrigger);

const track = document.getElementById('phasesTrack');

if (track) {
  const cards      = track.querySelectorAll('.phase-card');
  const cardWidth  = cards[0].offsetWidth + 28; // card + gap
  const totalScroll = cardWidth * (cards.length - 1);

  gsap.to(track, {
    x: () => -totalScroll,
    ease: 'none',
    scrollTrigger: {
      trigger: '.phases',
      pin: true,
      scrub: 0.8,
      start: 'top top',
      end: () => '+=' + (totalScroll + window.innerWidth * 0.3),
      invalidateOnRefresh: true,
    }
  });
}
