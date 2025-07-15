

from fastapi import APIRouter
from app.models.request_model import AdvertisingInput
from app.services.prediction import predict_sales

router = APIRouter()

@router.post("/predict")
def predict(input_data: AdvertisingInput):
    result = predict_sales(
        input_data.TV,
        input_data.radio,
        input_data.newspaper
    )
    return {"predicted_sales": round(result, 2)}

# FastAPI receives input, validates it using Pydantic, runs the prediction, and sends back a clean JSON response.