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

class PredictionResponse(BaseModel):
    milk_quality: float

class MilkModel():
    def __init__(self):
        self.model_name='../models/gnbayes.joblib'
        self.model=joblib.load(self.model_name)

    def predict_quality(self,pH,Temp,Taste,Odor,Fat,Turbidity,Colour):
        data_input=[[pH,Temp,Taste,Odor,Fat,Turbidity,Colour]]
        prediction=self.model.predict(data_input)
        probability=self.model.predict_proba(data_input).max()
        return prediction[0],probability

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
    input_data=data.model_dump()
    print(data)
    print(input_data)
    print("pH equal to:",input_data['pH']+5)
    pred = model.predict([[input_data['pH'],1,2,3,4,5,6]])[0] 
    print(pred)
    prediction=int(pred)

    return PredictionResponse(milk_quality=pred)
