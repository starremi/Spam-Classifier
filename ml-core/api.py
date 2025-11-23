from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path

app = FastAPI(title="Spam Classifier API")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow all origins (or restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL_PATH = Path("spam_classifier.pkl")
VECTORIZER_PATH = Path("tfidf_vectorizer.pkl")

class Message(BaseModel):
    message: str

@app.on_event("startup")
def load_model():
    global model, vectorizer
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

@app.post("/predict")
def predict(msg: Message):
    X = vectorizer.transform([msg.message])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]
    label = "spam" if pred == 1 else "ham"
    return {"label": label, "score": float(prob)}
