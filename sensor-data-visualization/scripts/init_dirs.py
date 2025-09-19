import os
from pathlib import Path

# folders to ensure exist
folders = [
    Path("data/raw"),
    Path("data/processed"),
    Path("notebooks"),
    Path("logs"),
    Path("scripts")
]

for p in folders:
    p.mkdir(parents=True, exist_ok=True)
    print(f"OK: {p.resolve()}")