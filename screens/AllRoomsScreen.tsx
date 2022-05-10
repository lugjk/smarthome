import { Switch } from "native-base";
import { useState, useEffect } from "react";
import { StyleSheet, TouchableOpacity } from "react-native";

import { Text, View } from "../components/Themed";
import { IRoom, User } from "../models/models";
import Rooms from "../mooks/rooms";
import { RootStackScreenProps } from "../types";
import { user } from "../context/userContext";

const convertTwoRow = (items: any[], amountInRow: number = 0) => {
  if (!items || items.length === 0) {
    return [];
  }

  const rows = items.reduce(function (rows, key, index) {
    return (
      (index % amountInRow === 0
        ? rows.push([key])
        : rows[rows.length - 1].push(key)) && rows
    );
  }, []);
  return rows;
};

export default function AllRoomScreen({
  navigation,
}: RootStackScreenProps<"AllRoomScreen">) {
  const [rooms, setRooms] = useState<IRoom[]>([])
  
  const getRooms = async () => {
     try {
      const response = await fetch('http://127.0.0.1:5000/rooms', {
        method: "GET",
        headers: {'Content-Type': 'application/json', "Authorization": user.token},
      });
       const json = await response.json();
       json.data.forEach((value: IRoom) => Rooms.push(value))
       setRooms(json.data)
       
    } catch (error) {
      console.error(error);
    } finally {
    }
  }

  useEffect(() => {
    getRooms()
  }, []);

  const data = convertTwoRow(rooms, 2);
  return (
    <View style={styles.relative}>
      <View style={styles.container}>
        {data.map((rows: any, index: number) => {
          return (
            <View style={styles.rowItem} key={index}>
              {rows.map((item: IRoom, index: number) => (
                <TouchableOpacity
                  key={index}
                  onPress={() => {
                    navigation.navigate("Root", {
                      screen: "TabHome",
                      params: { room: item },
                    });
                  }}
                  style={styles.item}
                >
                  <Text>{item.name}</Text>
                </TouchableOpacity>
              ))}
            </View>
          );
        })}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingVertical: 20,
    paddingHorizontal: 10,
    backgroundColor: "#f2f4f5",
  },
  relative: {
    flex: 1,
    position: "relative",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
  item: {
    flex: 1,
    backgroundColor: "#fff",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: 120,
    borderRadius: 20,
    marginLeft: 10,
    marginRight: 10,
  },
  rowItem: {
    display: "flex",
    flexDirection: "row",
    backgroundColor: "#f2f4f5",
    marginBottom: 20,
  },
  text: {
    fontSize: 16,
    color: "white",
    backgroundColor: "red",
    padding: 20,
    borderRadius: 20,
  },

  wapperBottom: {
    position: "absolute",
    bottom: 0,

    alignItems: "center",
    display: "flex",
    flex: 1,
    width: "100%",
  },
});
