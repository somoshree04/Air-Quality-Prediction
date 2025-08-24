from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model
model = joblib.load("aqi_model.pkl")

# Initialize FastAPI app
app = FastAPI(title="Air Quality Prediction API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all. Later you can restrict.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

# Define input schema
class AirQualityInput(BaseModel):
    PM2_5: float
    PM10: float
    NO2: float
    CO: float
    O3: float

@app.get("/")
def home():
    return {"message": "Welcome to the Air Quality Prediction API"}

@app.post("/predict")
def predict_air_quality(data: AirQualityInput):
    input_data = np.array([[data.PM2_5, data.PM10, data.NO2, data.CO, data.O3]])
    prediction = model.predict(input_data)[0]
    return {"AQI_Category": prediction}

