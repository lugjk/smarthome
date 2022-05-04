import EditScreenInfo from "../components/EditScreenInfo";
import { useState } from "react";
import { StyleSheet, TouchableOpacity } from "react-native";

import { Text, View } from "../components/Themed";
import { IDivice } from "../models/models";
import { RootStackScreenProps } from "../types";

export default function Setting({
  navigation,
}: RootStackScreenProps<"Setting">) {
  const [timesPressed, setTimesPressed] = useState(0);

  let textLog = "";
  if (timesPressed > 1) {
    textLog = timesPressed + "x onPress";
  } else if (timesPressed > 0) {
    textLog = "onPress";
  }
  return (
    <View style={styles.relative}>
      <View style={styles.container}>
        <View style={styles.separator}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("IDscreen");
            }}
            style={styles.item}
          >
            <Text>My ID</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.separator}>
          <TouchableOpacity
            onPress={() => {
              navigation.push("Login");
            }}
            style={styles.item}
          >
            <Text>Log out</Text>
          </TouchableOpacity>
        </View>
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
    backgroundColor: "#f2f4f5",
    flex: 1,
    position: "relative",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
  },
  separator: {
    marginTop: 30,
    marginBottom: 30,
    height: 120,
    width: "100%",
  },
  item: {
    backgroundColor: "white",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: 120,
    borderRadius: 20,
  },
  Box: {
    backgroundColor: "#f2f4f5",
    marginBottom: 20,
  },
  text: {
    fontSize: 200,
    color: "white",
    backgroundColor: "white",
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
