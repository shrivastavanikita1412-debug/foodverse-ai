# FoodVerse AI – Multimodal Food Intelligence Agent

A student-friendly full-stack prototype using React, FastAPI, Python, and OpenCV. This repository contains starter workflows for food-image analysis, freshness screening, hygiene checklists, recipe guidance, and personalised meal suggestions.

> **Limitations:** This is an educational prototype, not a medical, food-safety, or regulatory inspection system. Nutrition values are illustrative. A photo cannot establish that food is safe to eat or that a restaurant complies with regulations.

## Requirements
- Python 3.9+ (Python 3.11 recommended)
- Node.js 20+ and npm
- Visual Studio Code

## Run the backend
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Windows CMD: .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
Open http://127.0.0.1:8000/docs to explore the API.

## Run the React frontend
Open a second terminal:
```bash
cd frontend
npm install
npm run dev
```
Open the local URL printed by Vite (usually http://127.0.0.1:5173).

## Automated dependency verification
GitHub Actions runs a clean Python 3.11 environment, installs `requirements.txt`, checks dependency consistency with `pip check`, and verifies that the required packages and backend module import. See the [Verify Python requirements workflow](.github/workflows/verify-requirements.yml). A green workflow run is evidence of CI verification; it does not prove installation on your personal computer.

## Project modules
- Food recognition: image upload and OpenCV decoding; a trained classifier still needs to be connected.
- Nutrition: illustrative values; replace with a sourced nutrition database and serving-size logic.
- Freshness: conservative screening message; no validated freshness model is connected.
- Hygiene: transparent checklist scoring, not official compliance certification.
- Recipes and meal planning: starter rule-based suggestions; LLaMA integration is a future task.

## Skill Wallet evidence
See `tasks/skill-wallet-task-breakdown.md` for the six epics, activity subtasks, acceptance criteria, and evidence checklist. Complete tasks only after implementation and testing.

## Next steps
1. Choose and document a licensed food image dataset.
2. Train and evaluate a separate food classifier.
3. Connect a sourced nutrition database with serving sizes and uncertainty.
4. Build a freshness model only with appropriately labelled data; never present it as a safety guarantee.
5. Add automated tests, upload limits, error handling, and deployment configuration.
6. Capture screenshots, API results, and Git commits for Skill Wallet.
