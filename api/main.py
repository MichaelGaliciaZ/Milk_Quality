from fastapi import FastAPI
import joblib

app=FastAPI(
    title="Quality Milk Prediction API",
    description="An API for predicting the quality of milk.",
    version="1.0.0",
)
model=joblib.load('../models/gnbayes.joblib')

@app.get('/')
def predict(pH,Temp,Taste,Odor,Fat,Turbidity,Colour):
    """
    Milk Quality Predictions
    """
    print(pH,Temp,Taste,Odor,Fat,Turbidity,Colour)
    return {'result':pH+Temp}
