// 7 Type of Graph using React Native Chart Kit
// https://aboutreact.com/react-native-chart-kit/

// import React in our code
import { List } from "native-base";
import React, { useEffect, useState } from "react";
import AppLoading from 'expo-app-loading';

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

// const data = require("../api/data/switch.json");

const Graph1Room1 = () => {
  const [data, setData] = useState([]);
  const [dataGraph, setDataGraph] = useState([]);
  const [loading, setLoading] = useState(false);
  const [isEnabled, setIsEnabled] = useState(false);
  
  const getData = () => {
    fetch("https://io.adafruit.com/api/v2/Frost984/feeds/group-project.bbc-switch/data").then(
      res => res.json()
    ).then(
      data => {setData(data);}
    ).catch((error) => console.error(error))
  }

  const getDataGraph = () => {
    fetch("/switch/processdata").then(
      res => res.json()
    ).then(
      data => {setDataGraph(data); console.log(data), setLoading(true)}
    ).catch((error) => console.error(error))
  }

  useEffect(() => {
    getData()
    getDataGraph()
  },[])

  // if (!loading) {
  //   return (
  //     <AppLoading
  //     />
  //   );
  // }

 

  // useEffect(() => {
  //   fetch("/switch/data").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )

  // }, [])
  if (loading) {
    setIsEnabled(data[0]["value"] === "1")
  }
  const toggleSwitch = () => setIsEnabled((prevState) => !prevState);
  return (
    <>
      <Text style={styles.header}>Time spending</Text>
      <LineChart
        data={{
          labels: ["0", "6", "12", "18", "24"],
          datasets: [
            {
              data: dataGraph,
            },
          ],
        }}
        width={Dimensions.get("window").width - 16} // from react-native
        height={220}
        yAxisLabel={"used"}
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
    padding: 20,
    borderRadius: 20,
  },
});
export default Graph1Room1;
