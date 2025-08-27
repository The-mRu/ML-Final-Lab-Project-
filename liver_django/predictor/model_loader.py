# predictor/model_loader.py
import os, joblib, json, pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

_model = joblib.load(os.path.join(MODELS_DIR, "best_model.pkl"))
_scaler = joblib.load(os.path.join(MODELS_DIR, "scaler.pkl"))

with open(os.path.join(MODELS_DIR, "feature_names.json")) as f:
    _feature_names = json.load(f)

def predict_from_dict(input_dict):
    df = pd.DataFrame([input_dict], columns=_feature_names)
    X = _scaler.transform(df)
    pred = int(_model.predict(X)[0])
    proba = None
    if hasattr(_model, "predict_proba"):
        proba = float(_model.predict_proba(X)[0][1])
    return {"prediction": pred, "probability": proba}

