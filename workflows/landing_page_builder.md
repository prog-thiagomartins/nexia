# Workflow: Landing Page Builder

## Objective

Create animated, high-commercial-value landing pages using Claude Code as orchestrator, with Anime.js and GSAP for animations, following a structured and reproducible process.

## Required Inputs

- `project_name`: Project/product name
- `goal`: Page objective (lead capture, direct sale, event, etc.)
- `sections`: List of desired sections (hero, benefits, testimonials, CTA, etc.)
- `style_reference`: Reference URL or visual description (optional)
- `images`: Ready images or instruction to generate via `image_generation_pipeline.md`

## Tools

- Claude Code (main orchestrator)
- Anime.js — entrance animations, counters, text effects
- GSAP — horizontal scroll, magnetic mouse effects, parallax

## Process

### Step 1 — Define page structure

Before writing any code, define with the user:

1. Which sections the page will have and in what order
2. What the main CTA is (button, form, link)
3. Color palette and typography (or extract from reference)
4. Whether there will be horizontal scroll (creator's favorite effect — works well for features/pillars)

Document this in `.tmp/lp_brief_<project_name>.md` before proceeding.

### Step 2 — Project scaffolding

Create the file structure:

```
<project_name>/
├── index.html
├── css/
│   └── styles.css
├── js/
│   ├── animations.js    # Anime.js — entrance animations
│   ├── scroll.js        # GSAP — horizontal scroll and parallax
│   └── magnetic.js      # Magnetic mouse effect
├── images/
│   └── (generated via image_generation_pipeline.md)
└── assets/
    └── (fonts, icons)
```

Include Anime.js and GSAP via CDN in the HTML `<head>`:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
```

### Step 3 — Build HTML and CSS

1. Build semantic HTML for each section
2. Apply base CSS: layout, colors, typography, mobile responsiveness
3. Add animation classes (`data-animate`, `data-scroll`) to elements that will be animated — leave the effects for the next step

**Rule:** Mobile-first. The page must work well on mobile before any animation.

### Step 4 — Implement animations

Implement in layers, testing each one before moving on:

**Layer 1 — Entrance (Anime.js)**
```js
// Example: fade + slide up on elements with data-animate
anime({
  targets: '[data-animate]',
  opacity: [0, 1],
  translateY: [30, 0],
  duration: 800,
  delay: anime.stagger(100),
  easing: 'easeOutExpo'
});
```

**Layer 2 — Horizontal scroll (GSAP)**
```js
// For features/pillars sections
gsap.registerPlugin(ScrollTrigger);
gsap.to(".horizontal-track", {
  x: () => -(document.querySelector(".horizontal-track").scrollWidth - window.innerWidth),
  ease: "none",
  scrollTrigger: {
    trigger: ".horizontal-section",
    pin: true,
    scrub: 1,
    end: () => "+=" + document.querySelector(".horizontal-track").scrollWidth
  }
});
```

**Layer 3 — Magnetic mouse effect**
```js
// Buttons and interactive elements follow the cursor
document.querySelectorAll('.magnetic').forEach(el => {
  el.addEventListener('mousemove', (e) => {
    const rect = el.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    el.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
  });
  el.addEventListener('mouseleave', () => {
    el.style.transform = 'translate(0, 0)';
  });
});
```

### Step 5 — Images

If images are not yet ready, execute `image_generation_pipeline.md` now and apply the generated files to the `images/` folder.

### Step 6 — Final review

Checklist before considering the page done:

- [ ] Opens correctly on mobile and desktop
- [ ] Animations do not stutter on slower devices
- [ ] CTA is visible above the fold (without scrolling)
- [ ] Horizontal scroll works with trackpad and touch
- [ ] Images have background removed where necessary
- [ ] No errors in the browser console

## Outputs

- `<project_name>/` folder with all landing page files
- Functional, animated, and responsive page
- Ready for deployment via `deploy_site.md`

## Edge Cases

| Situation | How to handle |
|---|---|
| GSAP ScrollTrigger not working | Verify that the plugin was registered with `gsap.registerPlugin(ScrollTrigger)` |
| Slow animations on mobile | Reduce `duration` and disable magnetic effect on touch devices (`'ontouchstart' in window`) |
| Images without background available | Run `image_generation_pipeline.md` before continuing |
| Client wants CMS | Different scope — this workflow is for high-performance static pages |

## Video References

- Channel: Mateus Dias — "CLAUDE CODE + NANO BANANA PRO = Sites de R$10.000"
- Libraries used in production: Anime.js + GSAP
- Horizontal scroll effect validated on real pages with good conversion rates
