import pandas as pd

# Baca data cuaca
df = pd.read_csv(r"d:/Sekolah/UBM/Lomba/TechnoFest 2025/BanjirPredict/data/weather_data.csv")

# Hapus duplikat
df.drop_duplicates(inplace=True)

# Tangani missing values
df.fillna(0, inplace=True)  # Mengisi NaN dengan 0

# Konversi timestamp ke format datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Simpan data yang sudah dibersihkan
df.to_csv("../../data/weather_cleaned.csv", index=False)

print("✅ Data berhasil dibersihkan dan disimpan sebagai weather_cleaned.csv")
