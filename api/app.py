import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from model import MilkModel, milk_features

app = FastAPI()
model = MilkModel()

@app.get("/")
def index():
    return {"message": "Hello,stranger!"}

@app.post("/predict")
def predict_quality(milk: milk_features):
    data = milk.model_dump()
    print(data)
    print(jsonable_encoder(data))
    prediction, probability = model.predict_quality(pH=data['pH'], 
                                                    Temp=data['Temp'],
                                                    Taste=data['Taste'],
                                                    Odor=data['Odor'],
                                                    Fat=data['Fat'],
                                                    Turbidity=data['Turbidity'],
                                                    Colour=data['Colour']
    )
    return {
        'prediction':prediction,
        'probability':probability
    }

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8085)
