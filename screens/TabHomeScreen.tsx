import { StyleSheet } from "react-native";

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
  },
];

export default function TabHomeScreen({
  navigation,
}: RootTabScreenProps<"TabHome">) {
  return (
    <View style={styles.container}>
      <View style={styles.rowItem}>
        <View style={styles.item}>
          <Text>TV</Text>
        </View>
        <View style={styles.item}>
          <Text>PC</Text>
        </View>
      </View>
      <View style={styles.rowItem}>
        <View style={styles.item}>
          <Text>TV</Text>
        </View>
        <View style={styles.item}>
          <Text>PC</Text>
        </View>
      </View>
      <View style={styles.rowItem}>
        <View style={styles.item}>
          <Text>TV</Text>
        </View>
        <View style={styles.item}>
          <Text>PC</Text>
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