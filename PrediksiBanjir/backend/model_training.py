import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "temperature": [28, 30, 25, 27, 32, 24, 29],
    "humidity": [80, 85, 70, 75, 90, 60, 78],
    "rainfall": [100, 200, 50, 70, 300, 20, 150],
    "wind_speed": [10, 12, 5, 7, 15, 3, 9],
    "flood": [1, 1, 0, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop(columns=["flood"])
y = df["flood"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "flood_prediction_model.pkl")

print("Model berhasil dilatih dan disimpan!")
