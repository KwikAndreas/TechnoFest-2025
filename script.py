import requests

API_KEY = "6c91885585d027a8f40867741a974d61"
CITY = "Jakarta"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        print("✅ API Key Berfungsi!")
        print(f"Cuaca di {CITY}: {data['weather'][0]['description']}")
        print(f"Suhu: {data['main']['temp']}°C")
        print(f"Kelembapan: {data['main']['humidity']}%")
        print(f"Tekanan Udara: {data['main']['pressure']} hPa")
    elif response.status_code == 401:
        print("❌ API Key Tidak Valid atau Kadaluarsa!")
    elif response.status_code == 429:
        print("⚠️ Terlalu Banyak Permintaan! Coba Lagi Nanti.")
    else:
        print(f"⚠️ Error {response.status_code}: {data}")
except Exception as e:
    print(f"❌ Terjadi Kesalahan: {e}")
