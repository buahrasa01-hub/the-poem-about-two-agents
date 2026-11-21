from pathlib import Path
import os

poem = (
    "At the well, one grips",
    "the rusted handle down.",
    "The other wedges a boot",
    "against the loose stone.",
    "",
    "“On three,” says one.",
    "“I’ll brace,” says the other.",
    "",
    "They lift. The bucket",
    "comes up with both faces",
    "trembling in its black water.",
)
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text("\n".join(poem) + "\n", encoding="utf-8")
