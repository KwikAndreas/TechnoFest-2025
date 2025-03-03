import pandas as pd

# Baca data yang sudah dibersihkan
df = pd.read_csv("../../data/weather_cleaned.csv")

# Buat fitur baru
df["rain_intensity"] = df["rain"].apply(lambda x: "High" if x > 10 else "Medium" if x > 5 else "Low")
df["humidity_level"] = df["humidity"].apply(lambda x: "High" if x > 80 else "Medium" if x > 50 else "Low")

# Konversi fitur kategori menjadi numerik
df = pd.get_dummies(df, columns=["rain_intensity", "humidity_level"])

# Simpan data yang sudah diberi fitur
df.to_csv("../../data/weather_features.csv", index=False)

print("✅ Feature Engineering selesai. Data disimpan sebagai weather_features.csv")
