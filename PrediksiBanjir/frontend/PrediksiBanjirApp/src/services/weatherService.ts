import axios from "axios";

const API_KEY = "6c91885585d027a8f40867741a974d61";
const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

export const getWeatherData = async (latitude: number, longitude: number) => {
  try {
    const response = await axios.get(BASE_URL, {
      params: {
        lat: latitude,
        lon: longitude,
        units: "metric",
        appid: API_KEY,
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching weather data:", error);
    return null;
  }
};
