#!/usr/bin/env python3
"""Website wording for Widen 1.0.1: the free week starts by itself the first
time Widen widens a page (no 'Start free trial' button), and its start date is
kept in the iPhone's keychain rather than as an App Store transaction.
Apply only once 1.0.1 is live:  python3 tools/release-1.0.1.py && ./tools/stamp-css.sh"""
import pathlib, re

def edit(f, pairs):
    p = pathlib.Path(f); t = p.read_text()
    for old, new in pairs:
        t2, n = re.subn(old, lambda m: new, t, count=1, flags=re.S)
        assert n == 1, (f, old[:70])
        t = t2
    p.write_text(t)

edit('index.html', [
 (r' Back in the <em>Widen</em> app, start your free week; a tick shows against each step once it&rsquo;s done\.', ''),
 (r'<p class="deal-big">.*?</p>\n(\s*)<p>.*?</p>',
  '<p class="deal-big">Free for 7 days.<br>Then US$3.99 for lifetime access.</p>\n'
  '      <p>Nothing to start: just browse. Your free week begins the first time <em>Widen</em> widens a page, '
  'and reinstalling the app doesn&rsquo;t restart it. To keep <em>Widen</em> afterwards, buy it once in the app; '
  'it&rsquo;s then yours on every Duo signed in to your Apple Account. Outside the US, the App Store sets the '
  'equivalent price in your currency.</p>'),
])

edit('faq/index.html', [
 (r'Once <em>Widen</em> is allowed and your free week has started, every site',
  'Once <em>Widen</em> is allowed in Safari, every site'),
 (r'(<summary>When does the free week start\?</summary>\s*)<p>.*?</p>',
  '<summary>When does the free week start?</summary>\n        <p>By itself, the first time <em>Widen</em> widens a page. '
  'There&rsquo;s nothing to start. Deleting and reinstalling the app doesn&rsquo;t give you another week.</p>'),
 (r'(<summary>I have a second iPhone Duo\. Do I pay again\?</summary>\s*)<p>.*?</p>',
  '<summary>I have a second iPhone Duo. Do I pay again?</summary>\n        <p>No. Open the <em>Widen</em> app on the other Duo, '
  'signed in with the same Apple Account, and restore your purchase. If you haven&rsquo;t bought it yet, '
  'that Duo gets its own free week.</p>'),
])

edit('privacy/index.html', [
 (r'<li><strong>Your free trial and purchase</strong>:.*?</li>',
  '<li><strong>Your free week</strong>: the date it started is kept on your iPhone, in its keychain, so '
  'reinstalling doesn&rsquo;t restart it. It&rsquo;s never sent anywhere, and erasing the iPhone clears it.</li>\n'
  '      <li><strong>Your purchase</strong>: buying <em>Widen</em> is an App Store transaction, recorded by Apple '
  'against your Apple Account. <em>Widen</em> keeps a copy of its status on your iPhone so the Safari extension '
  'knows whether it may run.</li>'),
 (r'to check your free week and purchase\.', 'to check your purchase.'),
 (r'<p>The free week and the one-time purchase are handled by Apple',
  '<p>The one-time purchase is handled by Apple'),
 (r'Apple&rsquo;s own privacy policy covers them\.', 'Apple&rsquo;s own privacy policy covers it.'),
 (r'Last updated [0-9]+ [A-Za-z]+ 2026', 'Last updated ON_RELEASE'),
])
edit('index.html', [(r' <span class="soon">Next update</span>', '')])
edit('faq/index.html', [(r'<p>From the next update, yes\. In Control Center', '<p>Yes. In Control Center')])
print('1.0.1 wording applied. Set the privacy page date (ON_RELEASE), check, commit and push.')
