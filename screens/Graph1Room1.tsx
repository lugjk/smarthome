// 7 Type of Graph using React Native Chart Kit
// https://aboutreact.com/react-native-chart-kit/

// import React in our code
import React, { useState } from "react";

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

const Graph1Room1 = () => {
  const [isEnabled, setIsEnabled] = useState(false);
  const toggleSwitch = () => setIsEnabled((previousState) => !previousState);

  return (
    <>
      <Text style={styles.header}>Time spending</Text>
      <LineChart
        data={{
          labels: ["0 pm", "6 am", " 12 am", " 6 pm", "12 pm"],
          datasets: [
            {
              data: [8, 9, 2, 3, 6, 8],
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
    width: 20,
    height: 10,
  },
});
export default Graph1Room1;
