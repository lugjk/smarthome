/**
 * If you are not familiar with React Navigation, refer to the "Fundamentals" guide:
 * https://reactnavigation.org/docs/getting-started
 *
 */
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import {
  NavigationContainer,
  DefaultTheme,
  DarkTheme,
} from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import * as React from "react";
import { ColorSchemeName, Pressable, TouchableOpacity } from "react-native";

import Colors from "../constants/Colors";
import useColorScheme from "../hooks/useColorScheme";
import Graph1Room1 from "../screens/Graph1Room1";
import IDscreen from "../screens/IDscreen";

import LoginScreen from "../screens/LoginScreen";
import ModalScreen from "../screens/ModalScreen";
import NotFoundScreen from "../screens/NotFoundScreen";
import AllRoomsScreen from "../screens/AllRoomsScreen";
import Setting from "../screens/Setting";
import { RootStackParamList } from "../types";
import LinkingConfiguration from "./LinkingConfiguration";
import TabHomeScreen from "../screens/TabHomeScreen";
import { Text } from "../components/Themed";
import AntDesign from "@expo/vector-icons/AntDesign";
export default function Navigation({
  colorScheme,
}: {
  colorScheme: ColorSchemeName;
}) {
  return (
    <NavigationContainer
      linking={LinkingConfiguration}
      theme={colorScheme === "dark" ? DarkTheme : DefaultTheme}
    >
      <RootNavigator />
    </NavigationContainer>
  );
}

/**
 * A root stack navigator is often used for displaying modals on top of all other content.
 * https://reactnavigation.org/docs/modal
 */
const Stack = createNativeStackNavigator<RootStackParamList>();

function RootNavigator() {
  return (
    <Stack.Navigator initialRouteName="Login">
      <Stack.Screen
        name="Login"
        component={LoginScreen}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="Setting"
        component={Setting}
        options={{ title: "Account setting" }}
      />
      <Stack.Screen
        name="Root"
        component={TabHomeScreen}
        options={({ navigation }) => ({
          headerShown: true,
          title: " ",
          headerRight: () => (
            <TouchableOpacity onPress={() => navigation.navigate("Setting")}>
              <AntDesign name="setting" size={32} color="black" />
            </TouchableOpacity>
          ),
        })}
      />
      <Stack.Screen
        name="IDscreen"
        component={IDscreen}
        options={{
          headerShown: true,
          title: " ",
        }}
      />
      <Stack.Screen
        name="NotFound"
        component={NotFoundScreen}
        options={{ title: "Oops!" }}
      />
      <Stack.Screen
        name="AllRoomScreen"
        component={AllRoomsScreen}
        options={({ navigation }) => ({
          title: "Menu",
          headerBackVisible: false,
          headerRight: () => (
            <TouchableOpacity onPress={() => navigation.navigate("Setting")}>
              <AntDesign name="setting" size={32} color="black" />
            </TouchableOpacity>
          ),
        })}
      />
      <Stack.Screen
        name="Graph1Room1"
        component={Graph1Room1}
        options={({ navigation }) => ({
          title: "Graph1",
          headerBackVisible: true,
          headerRight: () => (
            <TouchableOpacity onPress={() => navigation.navigate("Setting")}>
              <AntDesign name="setting" size={32} color="black" />
            </TouchableOpacity>
          ),
        })}
      />
      <Stack.Group screenOptions={{ presentation: "modal" }}>
        <Stack.Screen name="Modal" component={ModalScreen} />
      </Stack.Group>
    </Stack.Navigator>
  );
}
