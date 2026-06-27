#!/usr/bin/env python3
"""
cleanup.py — remove LaTeX and pipeline transient files from application folders.

USAGE
    # after each xelatex compile (keeps .tex and .pdf)
    python scripts/cleanup.py clean --tex "applications/…/Ankur Desai Resume.tex"

    # also drop .pipeline/ mid-loop
    python scripts/cleanup.py clean --tex "…/Ankur Desai Resume.tex" --pipeline

    # final ship: LaTeX junk + .pipeline/ + legacy standalone JSON
    python scripts/cleanup.py clean --tex "…/Ankur Desai Resume.tex" --ship

    # maintenance: every resume under applications/
    python scripts/cleanup.py clean-tree --root applications
    python scripts/cleanup.py clean-tree --root applications --ship

    # stray pipeline JSON accidentally written to repo root
    python scripts/cleanup.py prune-root
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

_LATEX_ARTIFACT_SUFFIXES = (
    ".aux", ".bbl", ".blg", ".brf", ".dvi", ".fdb_latexmk", ".fls",
    ".idx", ".ilg", ".ind", ".lof", ".log", ".lot", ".nav", ".out",
    ".pdfsync", ".ps", ".run.xml", ".snm", ".synctex.gz", ".toc",
    ".upa", ".upb", ".vrb", ".xdv",
)
_LEGACY_JSON_NAMES = (
    "gate_inputs.json", "gate_report.json", "demerits.json", "demerit_score.json",
)


def _is_latex_artifact(path: Path) -> bool:
    name = path.name.lower()
    return any(name.endswith(suf) for suf in _LATEX_ARTIFACT_SUFFIXES)


def clean_latex_artifacts(tex_path: Path) -> list[str]:
    """Remove LaTeX intermediates next to the resume .tex; keep .tex and .pdf."""
    tex_path = Path(tex_path).resolve()
    parent = tex_path.parent
    stem = tex_path.stem
    prefix = stem + "."
    removed: list[str] = []
    for path in sorted(parent.iterdir()):
        if not path.is_file() or path == tex_path:
            continue
        if path.suffix.lower() == ".pdf" and path.stem == stem:
            continue
        if not path.name.startswith(prefix) or not _is_latex_artifact(path):
            continue
        path.unlink()
        removed.append(path.name)
    return removed


def clean_pipeline_artifacts(position_dir: Path, *, ship: bool = False) -> list[str]:
    """Remove transient pipeline files from a position folder."""
    position_dir = Path(position_dir).resolve()
    removed: list[str] = []
    pipeline_dir = position_dir / ".pipeline"
    if pipeline_dir.is_dir():
        shutil.rmtree(pipeline_dir)
        removed.append(".pipeline/")
    if ship:
        for name in _LEGACY_JSON_NAMES:
            path = position_dir / name
            if path.is_file():
                path.unlink()
                removed.append(name)
    return removed


def run_clean(args) -> int:
    tex = Path(args.tex).resolve()
    if not tex.is_file():
        print(f"clean: tex not found: {tex}", file=sys.stderr)
        return 1

    removed = clean_latex_artifacts(tex)
    if args.ship:
        removed.extend(clean_pipeline_artifacts(tex.parent, ship=True))
    elif args.pipeline:
        removed.extend(clean_pipeline_artifacts(tex.parent, ship=False))

    if removed:
        print(f"clean: removed {len(removed)} item(s) from {tex.parent}", file=sys.stderr)
        for name in removed:
            print(f"  {name}", file=sys.stderr)
    else:
        print(f"clean: nothing to remove in {tex.parent}", file=sys.stderr)

    if args.out:
        Path(args.out).write_text(json.dumps({"removed": removed}, indent=2), encoding="utf-8")
    return 0


def run_prune_root(args) -> int:
    root = Path(args.root).resolve()
    removed: list[str] = []
    for name in _LEGACY_JSON_NAMES:
        path = root / name
        if path.is_file():
            path.unlink()
            removed.append(name)
    if removed:
        print(f"prune-root: removed {len(removed)} item(s) from {root}", file=sys.stderr)
        for name in removed:
            print(f"  {name}", file=sys.stderr)
    else:
        print(f"prune-root: nothing to remove in {root}", file=sys.stderr)
    return 0


def run_clean_tree(args) -> int:
    root = Path(args.root).resolve()
    total: list[str] = []
    for tex in sorted(root.rglob("Ankur Desai Resume.tex")):
        total.extend(clean_latex_artifacts(tex))
        if args.ship:
            total.extend(clean_pipeline_artifacts(tex.parent, ship=True))
    print(f"clean-tree: removed {len(total)} item(s) under {root}", file=sys.stderr)
    for name in total:
        print(f"  {name}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Remove LaTeX and pipeline transient files.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    cl = sub.add_parser("clean", help="remove LaTeX build artifacts beside the resume")
    cl.add_argument("--tex", required=True, help="path to Ankur Desai Resume.tex")
    cl.add_argument("--pipeline", action="store_true",
                    help="also remove .pipeline/ transient dir")
    cl.add_argument("--ship", action="store_true",
                    help="full ship cleanup: .pipeline/ + legacy standalone JSON")
    cl.add_argument("--out", default="", help="optional JSON result path")
    cl.set_defaults(func=run_clean)

    ct = sub.add_parser("clean-tree", help="recursive clean under an applications root")
    ct.add_argument("--root", required=True, help="e.g. applications/")
    ct.add_argument("--ship", action="store_true", help="also remove pipeline + legacy JSON")
    ct.set_defaults(func=run_clean_tree)

    pr = sub.add_parser("prune-root", help="remove stray pipeline JSON from repo root")
    pr.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent.parent),
        help="repo root to prune (default: parent of scripts/)",
    )
    pr.set_defaults(func=run_prune_root)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
