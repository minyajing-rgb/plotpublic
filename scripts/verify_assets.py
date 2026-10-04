"""Verify the committed PNG library against its manifest and gallery."""

from pathlib import Path
from hashlib import sha256
from io import BytesIO
import json
import sys

from PIL import Image


root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "assets/manifest.json").read_text())
assets = manifest["assets"]
errors = []

if manifest["asset_count"] != len(assets):
    errors.append("manifest count differs from asset entries")

paths = set()
for asset in assets:
    rel = asset["path"]
    if rel in paths:
        errors.append(f"duplicate manifest path: {rel}")
    paths.add(rel)
    path = root / rel
    if not path.is_file():
        errors.append(f"missing image: {rel}")
        continue
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        errors.append(f"not a PNG: {rel}")
        continue
    if sha256(data).hexdigest() != asset["sha256"]:
        errors.append(f"hash mismatch: {rel}")
    if len(data) != asset["bytes"]:
        errors.append(f"size mismatch: {rel}")
    with Image.open(BytesIO(data)) as image:
        if (image.width, image.height) != (asset["width"], asset["height"]):
            errors.append(f"dimension mismatch: {rel}")
        image.verify()

actual = {str(p.relative_to(root)) for p in (root / "assets").rglob("*.png")}
if actual != paths:
    errors.append(f"PNG file set differs from manifest: {len(actual)} actual, {len(paths)} listed")

thumbs = sorted((root / "gallery/thumbs").glob("*.png"))
if len(thumbs) != len(assets):
    errors.append(f"thumbnail count {len(thumbs)} != asset count {len(assets)}")
if not (root / "gallery/index.html").is_file():
    errors.append("gallery/index.html missing")

for item in errors:
    print("ERROR", item, file=sys.stderr)
print(f"Verified {len(assets)} PNG assets and {len(thumbs)} thumbnails; {len(errors)} errors")
sys.exit(bool(errors))
