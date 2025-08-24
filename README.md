# Air-Quality-Prediction
A machine learning model with FastAPI and a simple frontend to predict Air Quality Index (AQI) categories. 
🌍 Air Quality Prediction

This project predicts the Air Quality Index (AQI) category (Good, Moderate, Unhealthy, etc.) based on pollutant levels (PM2.5, PM10, NO2, CO, O3).
It uses a Random Forest model, served through FastAPI backend, with a simple HTML + CSS + JavaScript frontend.

🚀 Features

Machine learning model trained on sample air quality dataset

FastAPI backend with /predict endpoint

Interactive frontend form for user input

Real-time prediction of AQI category

⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/air-quality-prediction.git
cd air-quality-prediction

2. Create virtual environment (optional but recommended)

python -m venv venv

3. Install dependencies

pip install -r requirements.txt(which includes fastapi, uvicorn, pandas, scikit-learn, joblib)

4. Run the backend (FastAPI)

uvicorn main:app --reload


Backend runs at: 👉 http://127.0.0.1:8000
Docs available at: 👉 http://127.0.0.1:8000/docs

5. Run the frontend

cd frontend
python -m http.server 5500


Frontend runs at: 👉 http://127.0.0.1:5500

📌 Future Developments(to be made)

Deploy backend to Render/Heroku and frontend to Netlify/Vercel

Use live AQI datasets for training

Add charts to visualize pollution levels


Create virtual environment (optional but recommended)

python -m venv venv
