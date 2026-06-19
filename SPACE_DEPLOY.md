Hugging Face Spaces — Deployment Helper
=====================================

This file contains quick commands and a small helper script to push this repo to a Hugging Face Space.

Steps to publish this repo as a Streamlit Space:

1. Install and login to the Hugging Face CLI (on your machine):

```bash
pip install --upgrade huggingface_hub
huggingface-cli login
# paste your HF token when prompted
```

2. Create the Space (replace `USERNAME`):

```bash
huggingface-cli repo create USERNAME/ai-travel-planner --type space --space-sdk streamlit
```

3. Add the HF remote and push from this `space` branch (commands below assume you are on the `space` branch):

```bash
# replace USERNAME with your HF username
git remote add hf https://huggingface.co/spaces/USERNAME/ai-travel-planner
git push hf space:main
```

4. In the Space settings (https://huggingface.co/spaces/USERNAME/ai-travel-planner/settings) add Secrets:

- `GEMINI_API_KEY` — your Gemini API key
- `OPENWEATHER_API_KEY` — if used

5. Open the Space URL shown in the web UI and monitor logs for build/runtime issues.

Helper script: `scripts/push_to_hf.sh`

This repo includes a convenience script you can run after logging in with `huggingface-cli`.

```bash
./scripts/push_to_hf.sh USERNAME
```

The script will create the remote `hf` (if missing) and push `space` to the Space `main` branch.

Notes
-----
- The app uses `GEMINI_API_KEY` by default; ensure that secret is set in the Space settings.
- Ollama is local-only; the Space should be configured to use `Gemini` in the UI or code.
