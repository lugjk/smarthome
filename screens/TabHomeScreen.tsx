import { StyleSheet, TouchableOpacity } from "react-native";

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
  function pushGarph() {
    navigation.push("Graph1Room1");
  }
  return (
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
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingVertical: 20,
    paddingHorizontal: 10,
    backgroundColor: "#f2f4f5",
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
});
