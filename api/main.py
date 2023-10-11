from fastapi import FastAPI
from model_utils import MilkModel, PredictionRequest, PredictionResponse

app = FastAPI(
    title="Quality Milk Prediction API",
    description="An API for predicting the quality of milk.",
    version="1.0.0",
)
model = MilkModel()


@app.post("/")
def predict(data: PredictionRequest):
    """
    Milk Quality Predictions
    """
    input_data = data.model_dump()
    print(data)
    print(input_data)
    print("pH equal to:", input_data["pH"] + 5)
    pred, proba = model.predict_quality(
        input_data["pH"],
        input_data["Temp"],
        input_data["Taste"],
        input_data["Odor"],
        input_data["Fat"],
        input_data["Turbidity"],
        input_data["Colour"],
    )
    print(pred, proba)
    prediction = int(pred)
    print(prediction)

    return PredictionResponse(milk_quality=pred, milk_quality_prob=proba)
