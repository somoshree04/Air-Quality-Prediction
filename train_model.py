import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("air_quality.csv")

# Features and target
X = df.drop(columns=["AQI_Category"]).values   # Convert to numpy array
y = df["AQI_Category"].values                  # Convert to numpy array

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Print accuracy
print("Model trained. Accuracy:", model.score(X_test, y_test))

# Save model
joblib.dump(model, "aqi_model.pkl")
