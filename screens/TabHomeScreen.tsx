import { useNavigation, useRoute } from "@react-navigation/native";
import React, { useEffect, useRef, useState } from "react";
import { Image, Pressable, StyleSheet, TouchableOpacity } from "react-native";

import EditScreenInfo from "../components/EditScreenInfo";
import AppIntroSlider from "../components/SliderIntro/Sliderintro";
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
  const slider = useRef<any>();
  const router = useRoute();
  console.log("router: ", router);

  useEffect(() => {
    slider.current && slider.current.goToSlide(2, true);
  }, []);

  let textLog = "";
  if (timesPressed > 1) {
    textLog = timesPressed + "x onPress";
  } else if (timesPressed > 0) {
    textLog = "onPress";
  }
  function pushGarph() {
    navigation.push("Graph1Room1");
  }

  const Rooms = [
    {
      Room: 1,
      title: "Room 1",
    },
    {
      Room: 2,
      title: "Room 2",
    },
    {
      Room: 3,
      title: "Room 3",
    },
  ];

  const renderItem = ({ item }: any) => {
    return (
      <View style={{ backgroundColor: "#f2f4f5" }}>
        <Text style={styles.title}>{item.title}</Text>
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
      </View>
    );
  };

  return (
    <View style={styles.relative}>
      <View style={styles.container}>
        <AppIntroSlider
          renderItem={renderItem}
          data={Rooms}
          ref={(ref) => (slider.current = ref)}
        />
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
    backgroundColor: "#f2f4f5",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    backgroundColor: "#f2f4f5",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
    backgroundColor: "#f2f4f5",
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
