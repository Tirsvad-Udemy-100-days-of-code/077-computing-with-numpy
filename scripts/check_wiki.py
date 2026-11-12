"""Check docs/wiki for twins, language lines, screenshots and the sidebar."""

from __future__ import annotations

import sys
from pathlib import Path

from computing_with_numpy.infrastructure.wiki_check import check_wiki

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "docs" / "wiki"
IMAGES = ROOT / "docs" / "images"


def main() -> int:
    """Print each problem and return 1 when there is any, else 0."""
    problems = check_wiki(WIKI, IMAGES)
    for problem in problems:
        sys.stdout.write(problem + "\n")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
