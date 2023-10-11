import joblib 
from pydantic import BaseModel

class MilkModel():
    def __init__(self):
        self.model_name='../models/gnbayes.joblib'
        self.model=joblib.load(self.model_name)

    def predict_quality(self,pH,Temp,Taste,Odor,Fat,Turbidity,Colour):
        data_input=[[pH,Temp,Taste,Odor,Fat,Turbidity,Colour]]
        prediction=self.model.predict(data_input)
        probability=self.model.predict_proba(data_input).max()
        return prediction[0],probability
    
class PredictionRequest(BaseModel):
    pH:float
    Temp:float
    Taste:float
    Odor:float
    Fat:float
    Turbidity:float
    Colour:float

class PredictionResponse(BaseModel):
    milk_quality: float
    milk_quality_prob:float