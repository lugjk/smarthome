// 7 Type of Graph using React Native Chart Kit
// https://aboutreact.com/react-native-chart-kit/

// import React in our code
import { useRoute } from "@react-navigation/native";
import React, { useEffect, useState } from "react";

// import all the components we are going to use
import {
  SafeAreaView,
  Switch,
  Text,
  View,
  StyleSheet,
  Dimensions,
  ScrollView,
} from "react-native";

//import React Native chart Kit for different kind of Chart
import { LineChart } from "react-native-chart-kit";
import { IDivice, IRoom } from "../models/models";
import Rooms from "../mooks/rooms";
import { RootStackScreenProps } from "../types";

const Graph1Room1 = ({ route }: RootStackScreenProps<"Graph1Room1">) => {
  const { params }: any = route.params;
  const [isEnabled, setIsEnabled] = useState(false);
  const toggleSwitch = () => setIsEnabled((previousState) => !previousState);

  const [divice, setDivice] = useState<IDivice>({
    id: 0,
    code: "",
    isON: false,
    name: "",
    type: "",
    time6: 0,
    time12: 0,
    time18: 0,
    time24: 0,
  });

  useEffect(() => {
    if (params) {
      const filterRoom = Rooms.find((item) => item.id === params.idRoom);
      const filter =
        filterRoom && filterRoom?.divices.find((item) => item.id === params.id);
      if (filter) {
        setDivice(filter);
      }
    }
  }, [params?.id]);

  return (
    <>
      <Text style={styles.header}>Time spending of {divice.code}</Text>
      {/* <Text style={styles.header}>Time spending of {item.code}</Text> */}
      <LineChart
        data={{
          labels: ["0 pm", "6 am", " 12 am", " 6 pm", "12 pm"],
          datasets: [
            {
              data: [
                0,
                divice.time6,
                divice.time12,
                divice.time18,
                divice.time24,
              ],
            },
          ],
        }}
        width={Dimensions.get("window").width - 16} // from react-native
        height={220}
        yAxisLabel={"hour"}
        chartConfig={{
          backgroundColor: "#1cc910",
          backgroundGradientFrom: "#eff3ff",
          backgroundGradientTo: "#efefef",
          decimalPlaces: 2, // optional, defaults to 2dp
          color: (opacity = 255) => `rgba(0, 0, 0, ${opacity})`,
          style: {
            borderRadius: 16,
          },
        }}
        bezier
        style={{
          marginVertical: 8,
          borderRadius: 16,
        }}
      />
      <View style={styles.containerbutton}>
        <Switch
          trackColor={{ false: "#767577", true: "#81b0ff" }}
          thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
          ios_backgroundColor="#3e3e3e"
          onValueChange={toggleSwitch}
          value={isEnabled}
        />
      </View>
    </>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "white",
    justifyContent: "center",
    alignItems: "center",
    textAlign: "center",
    padding: 10,
  },
  header: {
    textAlign: "center",
    fontSize: 18,
    padding: 16,
    marginTop: 16,
  },
  containerbutton: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});
export default Graph1Room1;
