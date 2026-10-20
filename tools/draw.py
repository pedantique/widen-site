#!/usr/bin/env python3
"""Draws the before/after pictures of the Duo's outer display as inline SVG
and puts them into index.html between the <!-- duo:before --> and
<!-- duo:after --> markers. Colours come from CSS variables in index.html,
so the pictures follow light and dark mode.

Geometry is the real one at 1 unit = 1 pt: a 466 x 678 display with Safari's
84 pt control strip on the right; without Widen the page stops at 382."""
import pathlib, re

def duo(wide, label, uid, notes=False):
    X, Y, W, H = 26, 26, 466, 678           # the display
    edge = X + (W if wide else 382)          # where the page's layout ends
    strip = X + 382                          # Safari's controls start here
    m = 18                                   # page margin
    right = edge - m if wide else edge - 14
    out = []
    a = out.append
    a(f'<svg class="duo" viewBox="0 0 518 730" role="img" aria-label="{label}">')
    a(f'<defs><clipPath id="scr-{uid}"><path d="M{X} {Y}h{W-44}a44 44 0 0 1 44 44v{H-88}a44 44 0 0 1-44 44h-{W-44}z"/></clipPath></defs>')
    # body: the hinge side is square, the free side rounded
    a(f'<path class="d-body" d="M8 4h444a62 62 0 0 1 62 62v598a62 62 0 0 1-62 62h-444a6 6 0 0 1-6-6v-710a6 6 0 0 1 6-6z"/>')
    a(f'<g clip-path="url(#scr-{uid})">')
    a(f'<rect class="d-screen" x="{X}" y="{Y}" width="{W}" height="{H}"/>')
    if not wide:
        a(f'<rect class="d-gutter" x="{strip}" y="{Y}" width="{W-382}" height="{H}"/>')
    # the page
    a(f'<rect class="d-photo" x="{X+m}" y="{Y+84}" width="{right-X-m}" height="176" rx="10"/>')
    sx = X + m + (right - X - m) * 0.72
    a(f'<circle class="d-sun" cx="{sx:.0f}" cy="{Y+134}" r="22"/>')
    a(f'<path class="d-hill" d="M{X+m} {Y+260}V{Y+214}q70-62 150-14t130 6q{(right-X-m-280)/2:.0f}-30 {right-X-m-280:.0f}-8V{Y+260}z"/>')
    a(f'<rect class="d-ink" x="{X+m}" y="{Y+282}" width="{right-X-m}" height="16" rx="5"/>')
    a(f'<rect class="d-ink" x="{X+m}" y="{Y+306}" width="{(right-X-m)*0.62:.0f}" height="16" rx="5"/>')
    y = Y + 346
    for i in range(14):
        short = i in (5, 13)
        w = (right - X - m) * (0.55 if short else 1)
        a(f'<rect class="d-text" x="{X+m}" y="{y}" width="{w:.0f}" height="7" rx="3.5"/>')
        y += 20 if i != 5 else 34
    # the site's fixed header: always ends at the strip, clear of the camera
    a(f'<rect class="d-bar" x="{X}" y="{Y}" width="{strip-X}" height="64"/>')
    a(f'<rect class="d-logo" x="{X+m}" y="{Y+24}" width="96" height="16" rx="4"/>')
    for k in range(3):
        a(f'<rect class="d-logo" x="{strip-46}" y="{Y+22+k*8}" width="24" height="4" rx="2"/>')
    # Safari's control strip, translucent, with the camera at the top
    a(f'<rect class="d-strip" x="{strip+10}" y="{Y+12}" width="{W-382-20}" height="{H-24}" rx="32"/>')
    a(f'<circle class="d-cam" cx="{strip+42}" cy="{Y+46}" r="17"/>')
    a(f'<circle class="d-lens" cx="{strip+42}" cy="{Y+46}" r="5"/>')
    for cy in (Y+300, Y+360, Y+606):
        a(f'<rect class="d-btn" x="{strip+30}" y="{cy}" width="24" height="24" rx="8"/>')
    a('</g>')
    if notes:  # numbered markers for the legend beside the picture
        for n, (cx, cy) in enumerate(((strip + 42, Y + 470), (strip - 12, Y + 64), (X + m + 40, Y + 560)), 1):
            a(f'<circle class="d-note" cx="{cx}" cy="{cy}" r="19"/>')
            a(f'<text class="d-note-n" x="{cx}" y="{cy + 7}" text-anchor="middle">{n}</text>')
    a('</svg>')
    return ''.join(out)

page = pathlib.Path(__file__).resolve().parent.parent / 'index.html'
html = page.read_text()
PICS = {
    'before': (False, 'Without Widen: the page stops where Safari’s buttons begin, leaving an empty band down the side', False),
    'after': (True, 'With Widen: text and pictures run to the edge of the display, under the buttons', False),
    'notes': (True, 'Widen at work, with three numbered points explained beside the picture', True),
}
for key, (wide, label, notes) in PICS.items():
    html = re.sub(rf'<!-- duo:{key} -->.*?<!-- /duo:{key} -->',
                  lambda _: f'<!-- duo:{key} -->{duo(wide, label, key, notes)}<!-- /duo:{key} -->', html, flags=re.S)
page.write_text(html)
