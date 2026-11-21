import os
from pathlib import Path

poem = """You pass the compass; I hold the map.
We fold them once, then choose north.
The road is neither yours nor mine—
two hands steer one lantern through fog.

The pact turns like a swallow:
not ownerless, not owned,
a hinge brightening between us,
either may open tomorrow."""

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(poem, encoding="utf-8")
