import React, { useState, useEffect } from "react";
import { View, Text, ActivityIndicator, Button } from "react-native";
import * as Location from "expo-location";
import { getWeatherData } from "../services/weatherService";
import { predictFlood } from "../services/floodService";

const HomeScreen = () => {
  const [weather, setWeather] = useState<any>(null);
  const [floodPrediction, setFloodPrediction] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== "granted") {
        console.error("Izin lokasi ditolak");
        return;
      }

      let location = await Location.getCurrentPositionAsync({});
      const weatherData = await getWeatherData(location.coords.latitude, location.coords.longitude);
      setWeather(weatherData);
      setLoading(false);

      if (weatherData) {
        const prediction = await predictFlood(
          weatherData.main.temp,
          weatherData.main.humidity,
          weatherData.rain ? weatherData.rain["1h"] || 0 : 0,
          weatherData.wind.speed
        );
        setFloodPrediction(prediction?.prediction || "Tidak diketahui");
      }
    })();
  }, []);

  if (loading) {
    return <ActivityIndicator size="large" />;
  }

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 20, fontWeight: "bold" }}>Cuaca Saat Ini</Text>
      <Text>Suhu: {weather?.main.temp}°C</Text>
      <Text>Kelembaban: {weather?.main.humidity}%</Text>
      <Text>Curah Hujan: {weather?.rain?.["1h"] || 0} mm</Text>
      <Text>Kecepatan Angin: {weather?.wind?.speed} m/s</Text>

      {floodPrediction && (
        <Text style={{ fontSize: 18, fontWeight: "bold", marginTop: 10 }}>
          Prediksi: {floodPrediction}
        </Text>
      )}

      <Button title="Lihat Peta" onPress={() => console.log("Navigasi ke Peta")} />
    </View>
  );
};

export default HomeScreen;
