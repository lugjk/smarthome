import { useNavigation } from "@react-navigation/native";
import React from "react";
import { Image, TouchableOpacity, View, ViewStyle } from "react-native";

import { StyleSheet } from "react-native";

import EditScreenInfo from "../components/EditScreenInfo";
import { Text } from "../components/Themed";

type Props = {
  item: any;
  style?: ViewStyle;
};

export default function BOxItem({ item }: Props) {
  const navigation = useNavigation();

  function navigateToArticle() {
    navigation.navigate(NavigatorScreen.ArticleScreen, {
      id: item.id,
      title: item.title,
    });
  }

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

  return (
    <View style={[styles.news, style]}>
      <TouchableOpacity
        style={styles.newsWrapper}
        onPress={navigateToArticle}
        activeOpacity={1}
      >
        <Image
          resizeMode="contain"
          style={styles.newsImage}
          source={{ uri: CommonHandle.urlImage(item.banner) }}
        />
        <Label size="xxs" weight="medium" numberOfLines={1}>
          {item.title}
        </Label>
        <Label size="xxxs" weight="normal" numberOfLines={3}>
          {item.description}
        </Label>
      </TouchableOpacity>
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
