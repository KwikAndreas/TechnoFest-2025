import React from "react";
import { View, Text } from "react-native";

const DetailScreen = ({ route }: any) => {
  const { weather } = route.params;

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 18, fontWeight: "bold" }}>Detail Prediksi Banjir</Text>
      <Text>Cuaca: {weather.weather[0].description}</Text>
      <Text>Suhu: {weather.main.temp}°C</Text>
      <Text>Kelembaban: {weather.main.humidity}%</Text>
      <Text>Tekanan Udara: {weather.main.pressure} hPa</Text>
      <Text>Kecepatan Angin: {weather.wind.speed} m/s</Text>
    </View>
  );
};

export default DetailScreen;
