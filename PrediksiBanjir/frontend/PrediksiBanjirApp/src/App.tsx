import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import HomeScreen from "./screen/HomeScreen";
import DetailScreen from "./screen/DetailScreen";

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: "Prediksi Banjir" }} />
        <Stack.Screen name="Detail" component={DetailScreen} options={{ title: "Detail Prediksi" }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
