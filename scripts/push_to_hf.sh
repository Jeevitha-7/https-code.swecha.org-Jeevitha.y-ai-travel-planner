#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 HF_USERNAME"
  exit 1
fi

HF_USER="$1"
HF_REMOTE="https://huggingface.co/spaces/${HF_USER}/ai-travel-planner"

echo "Adding remote 'hf' -> ${HF_REMOTE}' (if not present)"
if ! git remote get-url hf >/dev/null 2>&1; then
  git remote add hf "${HF_REMOTE}"
else
  echo "Remote 'hf' already exists. Updating URL to ${HF_REMOTE}."
  git remote set-url hf "${HF_REMOTE}"
fi

echo "Pushing branch 'space' to hf:main"
git push hf space:main

echo "Done. Visit https://huggingface.co/spaces/${HF_USER}/ai-travel-planner"
