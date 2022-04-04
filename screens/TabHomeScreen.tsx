import { useState } from "react";
import { Pressable, StyleSheet, TouchableOpacity } from "react-native";

import EditScreenInfo from "../components/EditScreenInfo";
import { Text, View } from "../components/Themed";
import { IDivice } from "../models/models";
import { RootTabScreenProps } from "../types";

const divices: IDivice[] = [
  {
    code: "smarttv",
    name: "SamSung 43 inch",
    type: "Smart TV",
    isON: false,
    Id: 5,
  },
];

export default function TabHomeScreen({
  navigation,
}: RootTabScreenProps<"TabHome">) {
  const [timesPressed, setTimesPressed] = useState(0);

  let textLog = "";
  if (timesPressed > 1) {
    textLog = timesPressed + "x onPress";
  } else if (timesPressed > 0) {
    textLog = "onPress";
  }
  function pushGarph() {
    navigation.push("Graph1Room1");
  }
  return (
    <View style={styles.relative}>
      <View style={styles.container}>
        <View style={styles.rowItem}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph1Room1");
            }}
            style={styles.item}
          >
            <Text>TV</Text>
          </TouchableOpacity>

          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph2Room1");
            }}
            style={styles.item}
          >
            <Text>PC</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.rowItem}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph1Room1");
            }}
            style={styles.item}
          >
            <Text>TV</Text>
          </TouchableOpacity>

          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph2Room1");
            }}
            style={styles.item}
          >
            <Text>PC</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.rowItem}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph1Room1");
            }}
            style={styles.item}
          >
            <Text>TV</Text>
          </TouchableOpacity>

          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph2Room1");
            }}
            style={styles.item}
          >
            <Text>PC</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.rowItem}>
          <TouchableOpacity
            onPress={() => {
              navigation.navigate("Graph1Room1");
            }}
            style={styles.item}
          >
            <Text>TV</Text>
          </TouchableOpacity>

          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph2Room1");
            }}
            style={styles.item}
          >
            <Text>PC</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.rowItem}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph1Room1");
            }}
            style={styles.item}
          >
            <Text>TV</Text>
          </TouchableOpacity>

          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph2Room1");
            }}
            style={styles.item}
          >
            <Text>PC</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.rowItem}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph3Room1");
            }}
            style={styles.item}
          >
            <Text>TV</Text>
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph4Room1");
            }}
            style={styles.item}
          >
            <Text>PC</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.rowItem}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph5Room1");
            }}
            style={styles.item}
          >
            <Text>TV</Text>
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Graph6Room1");
            }}
            style={styles.item}
          >
            <Text>PC</Text>
          </TouchableOpacity>
        </View>
      </View>
      <Pressable
        onPress={() => {
          setTimesPressed((current) => current + 1);
        }}
        style={({ pressed }) => [styles.wapperBottom]}
      >
        {({ pressed }) => (
          <Text style={styles.text}>
            {pressed ? "Recording!" : "Press me to record"}
          </Text>
        )}
      </Pressable>
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
