# Widen website

Static site for **Widen for iPhone Duo** (landing page, privacy policy, support),
served by GitHub Pages from `main` at <https://pedantique.github.io/widen-site/>.

- `index.html`: landing page. The App Store button is a placeholder (`id="app-store"`):
  set its `href` and remove `aria-disabled` once the app is live.
- `privacy/`: App Store privacy policy URL.
- `support/`: App Store support URL (widen@challis.com.au).
- `style.css`: shared styles, light and dark.
- `img/icon.png`, `img/apple-touch-icon.png`: resized from the app's
  `App/Assets.xcassets/AppIcon.appiconset/icon-1024.png`. Re-copy them if the icon changes:
  `sips -Z 360 <icon-1024.png> --out img/icon.png && sips -Z 180 <icon-1024.png> --out img/apple-touch-icon.png`
- `tools/draw.py`: draws the before/after pictures of the Duo's outer display as
  inline SVG into `index.html`. Run `python3 tools/draw.py` after changing it.

All links are relative, so the site works both at the github.io project path and on a custom domain.

<!--
Custom domain (planned: widen.challis.com.au)

1. DNS (GoDaddy, challis.com.au): add a CNAME record
       widen  ->  pedantique.github.io
   and wait until `dig +short widen.challis.com.au` shows GitHub's addresses
   (185.199.108-111.153).
2. Optional but recommended: verify challis.com.au for GitHub Pages
   (github.com/settings/pages → Add a domain), so nobody else can claim the subdomain.
3. Add the domain only after DNS works (otherwise github.io redirects to a dead name):
       echo widen.challis.com.au > CNAME && git add CNAME && git commit -m "Custom domain" && git push
   or Settings → Pages → Custom domain. Then tick "Enforce HTTPS" once the certificate is issued:
       gh api -X PUT repos/pedantique/widen-site/pages -F https_enforced=true
4. Update the App Store Connect privacy and support URLs to the new address.
-->
