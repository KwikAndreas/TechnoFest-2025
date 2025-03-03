from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model yang sudah dilatih
model = joblib.load("flood_prediction_model.pkl")

@app.route("/")
def home():
    return "API Prediksi Banjir Aktif"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Ambil nilai dari request
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    rainfall = data.get("rainfall")
    wind_speed = data.get("wind_speed")

    # Pastikan semua data tersedia
    if None in [temperature, humidity, rainfall, wind_speed]:
        return jsonify({"error": "Data tidak lengkap"}), 400

    # Format input data
    input_data = np.array([[temperature, humidity, rainfall, wind_speed]])

    # Lakukan prediksi
    prediction = model.predict(input_data)
    flood_risk = "Banjir" if prediction[0] == 1 else "Tidak Banjir"

    return jsonify({"prediction": flood_risk})

if __name__ == "__main__":
    app.run(debug=True)
