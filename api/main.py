from fastapi import FastAPI
from pydantic import BaseModel
import joblib

class ModelData(BaseModel):
    pH:float
    Temp:float
    Taste:float
    Odor:float
    Fat:float
    Turbidity:float
    Colour:float

app=FastAPI(
    title="Quality Milk Prediction API",
    description="An API for predicting the quality of milk.",
    version="1.0.0",
)
model=joblib.load('../models/gnbayes.joblib')

@app.post('/')
def predict(data:ModelData):
    """
    Milk Quality Predictions
    """
    print(data)
    return {'result':data}
