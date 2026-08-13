#!/usr/bin/env bash
# Idempotent bootstrap for the resume pipeline: XeLaTeX, CMU Serif, Python venv.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

need_tex=0
command -v xelatex >/dev/null 2>&1 || need_tex=1
# Query the family directly — do not `fc-list | grep -q` under pipefail (SIGPIPE → false miss).
[[ -n "$(fc-list 'CMU Serif' 2>/dev/null)" ]] || need_tex=1
# hyperref loads Zapf Dingbats (pzdr); missing it emergency-stops XeLaTeX
[[ -n "$(kpsewhich pzdr.tfm 2>/dev/null)" ]] || need_tex=1

if [[ "$need_tex" -eq 1 ]]; then
  if command -v apt-get >/dev/null 2>&1; then
    export DEBIAN_FRONTEND=noninteractive
    sudo apt-get update -qq
    sudo apt-get install -y --no-install-recommends \
      texlive-xetex \
      texlive-fonts-recommended \
      fonts-cmu \
      fontconfig \
      python3-venv \
      python3-pip
    fc-cache -f >/dev/null 2>&1 || true
  else
    echo "setup.sh: need xelatex and CMU Serif on PATH/fontconfig." >&2
    echo "  macOS: install MacTeX (or mactex-no-gui) so XeLaTeX can see CMU Serif." >&2
    echo "  Linux: sudo apt-get install texlive-xetex texlive-fonts-recommended fonts-cmu" >&2
    exit 1
  fi
fi

if [[ ! -x .venv/bin/python ]]; then
  python3 -m venv .venv
fi
.venv/bin/python -m pip install -q -r requirements.txt

echo "setup.sh: xelatex=$(command -v xelatex)  venv=.venv"
