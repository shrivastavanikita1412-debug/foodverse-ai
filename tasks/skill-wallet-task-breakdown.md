# FoodVerse AI — Skill Wallet Epic and Task Breakdown

Mark a task complete only after implementation and evidence are available.

## Epic 1 — Requirements Specification and Environment Setup
### Activity 1.1: Create requirements.txt
- [x] 1.1.1 List FastAPI, Uvicorn, python-multipart, OpenCV, NumPy and Pydantic.
- [x] 1.1.2 Document setup steps in README.
- [ ] 1.1.3 Verify installation in a clean virtual environment.
- Evidence: requirements file and successful install screenshot.
### Activity 1.2: Install libraries and set up virtual environment
- [ ] 1.2.1 Create and activate `.venv` with Python 3.9+.
- [ ] 1.2.2 Install requirements.
- [ ] 1.2.3 Start FastAPI and verify `/api/health` and `/docs`.
- Evidence: health response and Swagger UI screenshot.

## Epic 2 — Food Recognition & Nutrition
### Activity 2.1: Food image detection and classification
- [ ] 2.1.1 Implement validated image upload endpoint.
- [ ] 2.1.2 Decode image using OpenCV and handle corrupt files.
- [ ] 2.1.3 Select and document a licensed food image dataset.
- [ ] 2.1.4 Integrate a trained PyTorch classifier and confidence output.
- [ ] 2.1.5 Test valid, invalid, empty and oversized uploads.
- Evidence: API response, dataset source, model evaluation. Until the model is integrated, output must remain a labelled placeholder.
### Activity 2.2: Nutrition estimation and health scoring
- [ ] 2.2.1 Define serving-size and nutrition schemas.
- [ ] 2.2.2 Connect a documented nutrition source.
- [ ] 2.2.3 Estimate nutrients with portion assumptions.
- [ ] 2.2.4 Implement transparent scoring rules.
- [ ] 2.2.5 Test unknown foods and mixed dishes.
- Evidence: sample response, source and unit tests; avoid medical claims.

## Epic 3 — Food Freshness & Spoilage
### Activity 3.1: Preprocessing and feature extraction
- [ ] 3.1.1 Validate/decode images.
- [ ] 3.1.2 Resize and normalise consistently.
- [ ] 3.1.3 Document labelled dataset and splits.
- [ ] 3.1.4 Train/integrate a separate classifier only if suitable data exists.
- Evidence: preprocessing tests and model documentation.
### Activity 3.2: Freshness classification and recommendations
- [ ] 3.2.1 Define uncertainty-aware output schema.
- [ ] 3.2.2 Return unable-to-determine when no validated model is available.
- [ ] 3.2.3 Add cautious guidance from reputable food-safety sources.
- [ ] 3.2.4 Test blurry, low-light, unseen and corrupt images.
- Evidence: API tests. Never claim a photo proves food is safe.

## Epic 4 — Hygiene Monitoring and Smart Kitchen
### Activity 4.1: Hygiene detection and compliance scoring
- [ ] 4.1.1 Define observable checklist items.
- [ ] 4.1.2 Implement transparent score and missing-data handling.
- [ ] 4.1.3 Treat image detection as experimental, not certification.
- [ ] 4.1.4 Document privacy, consent and bias risks.
- [ ] 4.1.5 Test incomplete checklists.
- Evidence: score breakdown and tests; do not label it official compliance.
### Activity 4.2: Cooking guidance and recipe generation
- [ ] 4.2.1 Accept ingredients and diet preference.
- [ ] 4.2.2 Implement rule-based fallback.
- [ ] 4.2.3 Optionally integrate Meta LLaMA via an approved runtime/endpoint.
- [ ] 4.2.4 Validate outputs and safety claims.
- [ ] 4.2.5 Test empty inputs and unavailable model.
- Evidence: request/response examples; never commit API keys.

## Epic 5 — Personalised Meal Planner
### Activity 5.1: Profile, goals and preferences
- [ ] 5.1.1 Define goal, diet, allergies and disliked foods schema.
- [ ] 5.1.2 Validate inputs.
- [ ] 5.1.3 Add allergy exclusions and fallback handling.
- [ ] 5.1.4 Avoid storing profile data unless needed and disclosed.
- Evidence: schema tests and sample profile.
### Activity 5.2: Meal generation and adaptive recommendations
- [ ] 5.2.1 Generate daily plan.
- [ ] 5.2.2 Connect sourced nutrition and portion assumptions.
- [ ] 5.2.3 Rank suggestions against goals and exclusions.
- [ ] 5.2.4 Add feedback adaptation as an enhancement.
- [ ] 5.2.5 Test unsupported diets and excluded meals.
- Evidence: sample plan and tests; not medical advice.

## Epic 6 — Interface, Testing and Deployment
### Activity 6.1: Run core application
- [ ] 6.1.1 Start API with Uvicorn.
- [ ] 6.1.2 Verify all routes.
- [ ] 6.1.3 Add structured errors.
- Evidence: logs and API tests.
### Activity 6.2: React dashboard
- [ ] 6.2.1 Install dependencies and run Vite.
- [ ] 6.2.2 Add loading, success and error states.
- [ ] 6.2.3 Connect frontend actions to FastAPI.
- [ ] 6.2.4 Improve responsive layout and accessibility.
- [ ] 6.2.5 Add recipe form and hygiene checklist UI.
- Evidence: screenshots and successful browser/API flow.
### Activity 6.3: Validate and deploy
- [ ] 6.3.1 Test happy paths.
- [ ] 6.3.2 Test invalid uploads and unavailable backend.
- [ ] 6.3.3 Add automated tests.
- [ ] 6.3.4 Run frontend production build.
- [ ] 6.3.5 Finalise README and demo script.
- [ ] 6.3.6 Capture screenshots, commits and submission evidence.
- Evidence: test report, build output, README and demo.
