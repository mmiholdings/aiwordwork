from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_sentence
from calendar_gen import generate_hfw_calendar
from mbti import detect_mbti_type
from astrology import generate_natal_profile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to WordWeaver AI"}

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text")
    return analyze_sentence(text)

@app.post("/calendar")
async def calendar(request: Request):
    data = await request.json()
    return generate_hfw_calendar(data)

@app.post("/mbti")
async def mbti(request: Request):
    answers = await request.json()
    return detect_mbti_type(answers)

@app.post("/natal")
async def natal(request: Request):
    info = await request.json()
    return generate_natal_profile(info)
