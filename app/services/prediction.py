

import joblib
import numpy as np

# Load your model (ensure the path is correct)
model = joblib.load("app/services/regression_model.pkl")

def predict_sales(tv, radio, newspaper):
    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)
    return prediction[0]

# This function takes the input values, formats them correctly, and calls the model to make a prediction.