from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np

# Cargar el modelo guardado
model = joblib.load("mejor_modelo_logistic_regression.pkl")

# Instancia de FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de Predicción de Fraude Activa"}

@app.post("/predict")
def predict(data: dict):
    try:
        # Convertir el JSON recibido en un DataFrame
        df = pd.DataFrame([data])

        # Realizar la predicción
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        return {"fraud_prediction": int(prediction), "fraud_probability": float(probability)}
    except Exception as e:
        return {"error": str(e)}