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

import Graph2Room1 from "../screens/Graph2Room1";
import Graph3Room1 from "../screens/Graph3Room1";
import Graph4Room1 from "../screens/Graph4Room1";
import Graph5Room1 from "../screens/Graph5Room1";
import Graph6Room1 from "../screens/Graph6Room1";
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
              <AntDesign name="setting" size={32} color="green" />
            </TouchableOpacity>
          ),
        })}
      />
      <Stack.Screen
        name="IDscreen"
        component={IDscreen}
        options={({ navigation }) => ({
          headerShown: true,
          title: " ",
          headerRight: () => (
            <TouchableOpacity onPress={() => navigation.navigate("Setting")}>
              <AntDesign name="setting" size={32} color="green" />
            </TouchableOpacity>
          ),
        })}
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
              <AntDesign name="setting" size={32} color="green" />
            </TouchableOpacity>
          ),
        })}
      />
      <Stack.Screen
        name="Graph1Room1"
        component={Graph1Room1}
        options={({ navigation }) => ({
          title: "Graph1",
          headerBackVisible: false,
          headerRight: () => (
            <TouchableOpacity onPress={() => navigation.navigate("Setting")}>
              <AntDesign name="setting" size={32} color="green" />
            </TouchableOpacity>
          ),
        })}
      />
      <Stack.Screen
        name="Graph2Room1"
        component={Graph2Room1}
        options={{ title: "Graph2" }}
      />
      <Stack.Screen
        name="Graph3Room1"
        component={Graph3Room1}
        options={{ title: "Graph3" }}
      />
      <Stack.Screen
        name="Graph4Room1"
        component={Graph4Room1}
        options={{ title: "Graph4" }}
      />
      <Stack.Screen
        name="Graph5Room1"
        component={Graph5Room1}
        options={{ title: "Graph5" }}
      />
      <Stack.Screen
        name="Graph6Room1"
        component={Graph6Room1}
        options={{ title: "Graph6" }}
      />
      <Stack.Group screenOptions={{ presentation: "modal" }}>
        <Stack.Screen name="Modal" component={ModalScreen} />
      </Stack.Group>
    </Stack.Navigator>
  );
}
