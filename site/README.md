# genslate.github.io

Source for [genslate.github.io](https://genslate.github.io), Dustin Angeletti's developer profile site.

Plain HTML, CSS and JavaScript: no framework and no build step.

| File | What it is |
| --- | --- |
| `index.html` | The page: hero, about, stack, work, contact |
| `styles.css` | Nord palette, dark and light themes, layout and reveal animations |
| `main.js` | Interactive particle field, theme toggle, rotating role, scroll reveals |
| `404.html` | Page GitHub Pages serves for missing URLs |
| `assets/` | Brand mark, SLATESUITE screenshot, social preview image |

## Run locally

```sh
cd site
python3 -m http.server 8000
# open http://localhost:8000
```

## Publish at genslate.github.io

GitHub serves the root domain only from a repository named exactly `genslate.github.io`.

1. Create a public repository named `genslate.github.io` on the GENSLATE account.
2. Copy everything in this folder (including the hidden `.nojekyll`) to the root of that repository and push to `main`.
3. In that repository, open **Settings → Pages** and set **Source** to *Deploy from a branch*, branch `main`, folder `/ (root)`.

The site goes live at https://genslate.github.io within a minute or two.

## Particle field

A jittered grid of capsule particles. A focal point eases toward the pointer (or wanders when idle);
particles near a breathing ring around it brighten, stretch, turn to face it and get pushed outward,
then spring back. Colour follows the angle around the focus through the Nord frost and aurora
palettes. Clicking sends a shockwave. Particles are batched into ~200 strokes per frame, the loop
pauses in background tabs, and `prefers-reduced-motion` gets a single static frame.
