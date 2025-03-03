import axios from "axios";

const BACKEND_URL = "http://127.0.0.1:5000";

export const predictFlood = async (temperature: number, humidity: number, rainfall: number, wind_speed: number) => {
  try {
    const response = await axios.post(`${BACKEND_URL}/predict`, {
      temperature,
      humidity,
      rainfall,
      wind_speed,
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching prediction:", error);
    return null;
  }
};
