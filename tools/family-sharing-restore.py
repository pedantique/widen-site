#!/usr/bin/env python3
"""Puts the Family Sharing wording back once Widen for Life is family-shareable
in App Store Connect. Run from the repo root: python3 tools/family-sharing-restore.py"""
import json, pathlib
for r in json.loads(pathlib.Path('tools/family-sharing.json').read_text()):
    p = pathlib.Path(r['file']); s = p.read_text()
    if r['was'] in s: continue
    if r['now']:
        assert r['now'] in s, r; s = s.replace(r['now'], r['was'], 1)
    else:  # removed block: put it back after its anchor
        anchor = r['anchor']; assert anchor in s, r; s = s.replace(anchor, anchor + r['was'], 1)
    p.write_text(s)
print('Family Sharing wording restored')
