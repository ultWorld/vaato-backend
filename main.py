import os
from os.path import join, dirname
import traceback
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# import base64
from fastapi import Body, FastAPI, UploadFile, Form, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware


import logging

logging.basicConfig(level=logging.INFO)

from src.utils.audio import convert_audio_to_base64
from src.brokers import email
from src.routes.interview import analysis
from src.routes.interview import feedback
from src.routes.interview import interview
from src.routes.hr_campaign import gen_metric

# Preload AI models
# stt_model = whisper.load_model("small")

app = FastAPI(
    title="Vaato Backend",
    version="1.0.1",
)

origins = [
    "http://localhost:3000",
    "https://ai-interviewer-two.vercel.app",
    "https://vaato.vercel.app",
    "https://vaato.ultimateworld.io",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis.router)
app.include_router(email.router)
app.include_router(feedback.router)
app.include_router(interview.router)
app.include_router(gen_metric.router)

