from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import cv2
import numpy as np
from backend.services.hygiene import score_hygiene
from backend.services.planner import build_meal_plan, make_recipe

app = FastAPI(title="FoodVerse AI API", description="Educational prototype for multimodal food intelligence.", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_UPLOAD_BYTES = 8 * 1024 * 1024

@app.get("/")
def root(): return {"name":"FoodVerse AI", "status":"running", "docs":"/docs"}

@app.get("/api/health")
def health(): return {"status":"ok", "service":"FoodVerse AI API"}

async def read_image(file: UploadFile):
    if file.content_type not in ALLOWED_TYPES: raise HTTPException(415, "Upload a JPG, PNG, or WEBP image.")
    data = await file.read()
    if not data: raise HTTPException(400, "The uploaded file is empty.")
    if len(data) > MAX_UPLOAD_BYTES: raise HTTPException(413, "Image must be 8 MB or smaller.")
    image = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
    if image is None: raise HTTPException(400, "Could not decode image. Try a valid JPG or PNG.")
    return image

@app.post("/api/food/analyse")
async def food_analyse(file: UploadFile = File(...)):
    image = await read_image(file)
    h,w = image.shape[:2]
    return {"module":"food-recognition", "status":"prototype", "image":{"width":w,"height":h}, "prediction":{"label":"unidentified food", "confidence":None, "note":"No trained classifier is connected; this is not an AI prediction."}, "nutrition_examples":{"apple":{"calories_kcal":95,"protein_g":0.5,"carbs_g":25,"fat_g":0.3},"banana":{"calories_kcal":105,"protein_g":1.3,"carbs_g":27,"fat_g":0.4},"rice":{"calories_kcal":205,"protein_g":4.3,"carbs_g":45,"fat_g":0.4}}, "health_score":None}

@app.post("/api/freshness/screen")
async def freshness_screen(file: UploadFile = File(...)):
    image = await read_image(file)
    h,w = image.shape[:2]
    return {"module":"freshness-screening", "status":"prototype", "image":{"width":w,"height":h}, "visual_freshness_prediction":None, "message":"No validated freshness model is connected. Appearance cannot establish food safety.", "recommendation":"Check storage history and reliable food-safety guidance. When in doubt, discard."}

class HygieneRequest(BaseModel):
    handwashing_station: bool
    surfaces_clean: bool
    food_covered: bool
    raw_and_cooked_separated: bool
    temperature_logs_available: bool

@app.post("/api/hygiene/score")
def hygiene_score(payload: HygieneRequest): return score_hygiene(payload.model_dump())

class MealRequest(BaseModel):
    goal: str = Field(default="balanced", max_length=40)
    diet: str = Field(default="vegetarian", max_length=40)
    allergies: list[str] = Field(default_factory=list, max_length=20)
    disliked_foods: list[str] = Field(default_factory=list, max_length=30)

@app.post("/api/meals/plan")
def meal_plan(payload: MealRequest): return build_meal_plan(payload.goal, payload.diet, payload.allergies, payload.disliked_foods)

class RecipeRequest(BaseModel):
    ingredients: list[str] = Field(min_length=1, max_length=20)
    diet: str = Field(default="vegetarian", max_length=40)

@app.post("/api/recipes/suggest")
def recipe_suggest(payload: RecipeRequest): return make_recipe(payload.ingredients, payload.diet)
