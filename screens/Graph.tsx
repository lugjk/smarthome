// 7 Type of Graph using React Native Chart Kit
// https://aboutreact.com/react-native-chart-kit/

// import React in our code
import { useRoute } from "@react-navigation/native";
import React, { useEffect, useState } from "react";
// import {mqtt_callbacks, mqtt_client, relay_feed} from "../mqtt_connection";
// import all the components we are going to use
import {
  Switch,
  Text,
  View,
  StyleSheet,
  Dimensions,
} from "react-native";

//import React Native chart Kit for different kind of Chart
import { BarChart } from "react-native-chart-kit";
import { user } from "../context/userContext";
import { IDevice} from "../models/models";
import { RootStackScreenProps } from "../types";

const Graph = ({ route }: RootStackScreenProps<"Graph">) => {
  const { params }: any = route.params;
  const [device, setDevice] = useState<IDevice>({
    _id: "",
    code: "",
    isON: false,
    name: "",
    category: "",
  });
  const [data, setData] = useState<number[]>([1,2,3,4,5,6,7]);

  const [switchState, setSwitchState] = useState<boolean>(device.isON)

  const getTimeUsed = async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/devices/data/' + params.device._id, {
          method: "GET",
          headers: {'Content-Type': 'application/json', "Authorization": user.token},
        });
        
        const json = await response.json();
        setData(json.data)

      
      } catch (error) {
        console.error(error);
      } finally {
        // setLoading(false);
      }

  }

  useEffect(() => {
    if (params) {
        setDevice(params.device);
        getTimeUsed()
    }
  }, [params?.device]);

  const toggleSwitch = (value: boolean) => {
    {
      device.isON = value;
      setDevice(device);
      setSwitchState(value)
      // const mqtt_message = value ? "1" : "0";
  	  // mqtt_client.publish(relay_feed, mqtt_message);
    }
  };

  // mqtt_callbacks[relay_feed] = (payload: number) => {
  //   const newState = payload.toString() === "1";
  //   toggleSwitch(newState)
  // }

  return (
    <>
      <Text style={styles.header}>Time spending of {device.name}</Text>
      <View style={styles.graph}>
        <BarChart
          data={{
            labels: ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"],
            datasets: [
                {
                  data: data
                }
              ]
            }}
          width={Dimensions.get("window").width * 0.95} // from react-native
          height={220}
          yAxisLabel=""
          yAxisSuffix="h"
          yAxisInterval={1} // optional, defaults to 1
          chartConfig={{
            backgroundColor: "#e26a00",
            backgroundGradientFrom: "#fb8c00",
            backgroundGradientTo: "#ffa726",
            decimalPlaces: 2, // optional, defaults to 2dp
            color: (opacity = 0.5) => `rgba(255, 255, 255, ${opacity})`,
            labelColor: (opacity = 0.5) => `rgba(255, 255, 255, ${opacity})`,
            style: {
              borderRadius: 16
            },
            propsForDots: {
              r: "6",
              strokeWidth: "2",
              stroke: "#ffa726"
            }
          }}
          style={{
            marginVertical: 8,
            borderRadius: 16
          }}
        />
      </View>
      <View style={styles.containerbutton}>
        <Switch
          trackColor={{ false: "#767577", true: "#81b0ff" }}
          thumbColor={device.isON ? "#f5dd4b" : "#f4f3f4"}
          ios_backgroundColor="#3e3e3e"
          onValueChange={(value) => {
            toggleSwitch(value);
          }}
          value={switchState}
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
  graph: {
    alignItems: "center",
  }
});
export default Graph;
