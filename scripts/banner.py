"""Generate the animated profile banner (assets/banner.svg).

A flat Nord plate with a ring field of small capsule particles that
point toward a focal point, breathe, and slowly orbit. Pure SVG + CSS
so it animates inside GitHub's <img> sandbox (no scripts, no fonts).
"""
import math
import random

random.seed(7)
W, H = 1200, 320
CX, CY = 930, 160  # focal point of the particle field

FROST = ["#8fbcbb", "#88c0d0", "#81a1c1", "#5e81ac"]
AURORA = ["#bf616a", "#d08770", "#ebcb8b", "#a3be8c", "#b48ead"]

rings = []
for r_i, radius in enumerate(range(46, 330, 22)):
    count = int(radius * 0.34)
    dashes = []
    for k in range(count):
        a = (k / count) * math.tau + random.uniform(-0.08, 0.08) + r_i * 0.37
        rr = radius + random.uniform(-6, 6)
        x = CX + math.cos(a) * rr
        y = CY + math.sin(a) * rr * 0.62  # squash into an ellipse
        if not (-10 < x < W + 10 and -10 < y < H + 10):
            continue
        ang = math.degrees(math.atan2(CY - y, CX - x))
        length = max(3.0, 11 - r_i * 0.55) + random.uniform(-1, 1)
        # colour: frost near the core, aurora sparks sprinkled outward
        if random.random() < 0.10 + r_i * 0.012:
            col = random.choice(AURORA)
        else:
            col = FROST[min(len(FROST) - 1, r_i // 4)]
        op = max(0.18, 0.95 - r_i * 0.055) * random.uniform(0.7, 1)
        dashes.append((x, y, ang, length, col, op))
    rings.append(dashes)

out = []
out.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Dustin Angeletti · GENSLATE</title>
  <desc id="d">Developer, engineer, AI. A field of small particles orbits a glowing core on a dark Nord background.</desc>
  <style>
    .ring {{ transform-box: view-box; transform-origin: {CX}px {CY}px; animation: orbit linear infinite, breathe ease-in-out infinite alternate; }}
    .core {{ transform-box: fill-box; transform-origin: center; animation: pulse 3.2s ease-in-out infinite alternate; }}
    .fade {{ animation: rise 1.1s cubic-bezier(.2,.7,.2,1) both; }}
    .fade.d2 {{ animation-delay: .15s; }}
    .fade.d3 {{ animation-delay: .3s; }}
    .caret {{ animation: blink 1s steps(1) infinite; }}
    @keyframes orbit {{ to {{ rotate: 360deg; }} }}
    @keyframes breathe {{ from {{ scale: 1; }} to {{ scale: 1.045; }} }}
    @keyframes pulse {{ from {{ opacity: .55; scale: .92; }} to {{ opacity: 1; scale: 1.08; }} }}
    @keyframes rise {{ from {{ opacity: 0; translate: 0 14px; }} }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ring, .core, .fade, .caret {{ animation: none; }} }}
    text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Ubuntu, Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, "JetBrains Mono", Menlo, Consolas, monospace; }}
  </style>
  <defs>
    <radialGradient id="glow" cx="{CX / W:.3f}" cy="0.5" r="0.42">
      <stop offset="0" stop-color="#88c0d0" stop-opacity=".22"/>
      <stop offset="1" stop-color="#88c0d0" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="plate"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#plate)">
    <rect width="{W}" height="{H}" fill="#2e3440"/>
    <rect width="{W}" height="{H}" fill="url(#glow)"/>''')

for i, dashes in enumerate(rings):
    dur = 90 + i * 14
    direction = "normal" if i % 2 == 0 else "reverse"
    bdur = 3.4 + (i % 5) * 0.45
    out.append(
        f'    <g class="ring" style="animation-duration:{dur}s,{bdur:.2f}s;'
        f'animation-direction:{direction},alternate" stroke-linecap="round" stroke-width="2.6">'
    )
    for x, y, ang, length, col, op in dashes:
        dx = math.cos(math.radians(ang)) * length / 2
        dy = math.sin(math.radians(ang)) * length / 2
        out.append(
            f'      <line x1="{x - dx:.1f}" y1="{y - dy:.1f}" x2="{x + dx:.1f}" y2="{y + dy:.1f}" '
            f'stroke="{col}" stroke-opacity="{op:.2f}"/>'
        )
    out.append("    </g>")

out.append(f'''    <circle class="core" cx="{CX}" cy="{CY}" r="9" fill="#88c0d0"/>
    <circle cx="{CX}" cy="{CY}" r="3.5" fill="#eceff4"/>

    <g transform="translate(34 58) scale(.105)">
      <path d="M282 595 L512 727 L512 761 L282 629 Z" fill="#4c6a8f"/>
      <path d="M512 727 L742 595 L742 629 L512 761 Z" fill="#3e5878"/>
      <path d="M512 463 L742 595 L512 727 L282 595 Z" fill="#5e81ac"/>
      <path d="M282 495 L512 627 L512 661 L282 529 Z" fill="#6983a0"/>
      <path d="M512 627 L742 495 L742 529 L512 661 Z" fill="#566d88"/>
      <path d="M512 363 L742 495 L512 627 L282 495 Z" fill="#81a1c1"/>
      <path d="M282 395 L512 527 L512 561 L282 429 Z" fill="#6c9ba9"/>
      <path d="M512 527 L742 395 L742 429 L512 561 Z" fill="#5a8390"/>
      <path d="M512 263 L742 395 L512 527 L282 395 Z" fill="#88c0d0"/>
    </g>
    <text class="fade mono" x="126" y="117" fill="#88c0d0" font-size="16" letter-spacing="4">GENSLATE</text>
    <text class="fade d2" x="64" y="200" fill="#eceff4" font-size="54" font-weight="700" letter-spacing="-1">Dustin Angeletti</text>
    <text class="fade d3 mono" x="66" y="244" fill="#d8dee9" font-size="18">Developer · Engineer · AI<tspan class="caret" fill="#88c0d0"> ▍</tspan></text>
  </g>
</svg>''')

import sys
open(sys.argv[1], "w").write("\n".join(out) + "\n")
print(sum(len(r) for r in rings), "particles")
