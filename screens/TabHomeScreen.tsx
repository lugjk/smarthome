import { Switch } from "native-base";
import React, { useEffect, useState } from "react";
import { Pressable, StyleSheet, TouchableOpacity } from "react-native";

import AppIntroSlider from "../components/SliderIntro/Sliderintro";
import { Text, View } from "../components/Themed";
import { IDivice, IRoom } from "../models/models";
import divices from "../mooks/devices";
import Rooms from "../mooks/rooms";
import { RootTabScreenProps } from "../types";

import { Audio } from 'expo-av';
import * as FileSystem from 'expo-file-system';


const convertTwoRow = (items: any[], amountInRow: number = 0) => {
  if (!items || items.length === 0) {
    return [];
  }
  const rows = items.reduce(function (rows, key, index) {
    return (
      (index % amountInRow === 0
        ? rows.push([key])
        : rows[rows.length - 1].push(key)) && rows
    );
  }, []);
  return rows;
};

export default function TabHomeScreen({
  navigation,
  route,
}: RootTabScreenProps<"TabHome">) {
  const [timesPressed, setTimesPressed] = useState(0);
  const { params }: any = route.params;
  const [room, setRoom] = useState<IRoom>({
    id: 0,
    title: "",
    divices: [],
  });

  useEffect(() => {
    const filter = Rooms.find((item) => item.id === params.id);
    if (filter) {
      setRoom(filter);
    }
  }, [params.id]);

  let textLog = "";
  if (timesPressed > 1) {
    textLog = timesPressed + "x onPress";
  } else if (timesPressed > 0) {
    textLog = "onPress";
  }

  const toggleSwitch = (id: number, value: boolean) => {
    room.divices.map((y) => {
      if (y.id === id) {
        y.isON = !value;
      }
      return y;
    });
    setRoom(room);
  };

  const rdevices = convertTwoRow(divices, 2);  
  const [recording, setRecording] = useState();
  async function startRecording() {
    if (recording == null){
    try {
      console.log('Requesting permissions..');
      await Audio.requestPermissionsAsync();
      await Audio.setAudioModeAsync({
        allowsRecordingIOS: true,
        playsInSilentModeIOS: true,
      }); 
      console.log('Starting recording..');
      const { recording } = await Audio.Recording.createAsync(
         Audio.RECORDING_OPTIONS_PRESET_HIGH_QUALITY
      );
      setRecording(recording);
      console.log('Recording started');
    } catch (err) {
      console.error('Failed to start recording', err);
    }
   }
  }
  
  async function stopRecording() {
    console.log('Stopping recording..');
    setRecording(undefined);
    await recording.stopAndUnloadAsync();
    const uri = recording.getURI(); 
    console.log('Recording stopped and stored at', uri);
    //Playback the recorded sound for debugginh
    /*const {sound} = await Audio.Sound.createAsync({
  		uri: uri,
  });
    console.log("Playing Sound");
    await sound.playAsync();*/
    
    console.log("Sending record file to server");
    const serverUrl = "https://test-dadn.free.beeceptor.com";
    await FileSystem.uploadAsync(serverUrl, uri);
}

  const renderItem = ({ item }: any) => {
    return (
      <View style={{ backgroundColor: "#f2f4f5" }}>
        <Text style={styles.title}>{item.title}</Text>
        {rdevices.map((rows: any, index: number) => {
          return (
            <View style={styles.rowItem} key={index}>
              {rows.map((item: IDivice, index: number) => {
                return (
                  <TouchableOpacity
                    key={index}
                    onPress={() => {
                      navigation.navigate("Graph1Room1", {
                        screen: "Graph1Room1",
                        params: {
                          id: item.id,
                          idRoom: room.id,
                        },
                      });
                    }}
                    style={styles.item}
                  >
                    <Text>{item.code}</Text>
                    <View style={styles.containerbutton}>
                      <Switch
                        trackColor={{ false: "#767577", true: "#81b0ff" }}
                        thumbColor={item.isON ? "#f5dd4b" : "#f4f3f4"}
                        ios_backgroundColor="#3e3e3e"
                        onValueChange={(value) => toggleSwitch(item.id, value)}
                        value={item.isON}
                      />
                    </View>
                  </TouchableOpacity>
                );
              })}
            </View>
          );
        })}
      </View>
    );
  };

  return (
    <View style={styles.relative}>
      <View style={styles.container}>
        {room.id ? (
          <AppIntroSlider
            renderItem={renderItem}
            data={Rooms}
            initialIndex={Rooms.findIndex((item) => item.id === room.id)}
          />
        ) : null}
      </View>
      <Pressable
        onPress={() => {
          setTimesPressed((current) => current + 1);
        }}
        onPressIn={startRecording}
        onPressOut={stopRecording}
        
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
    marginBottom: 20,
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
  containerItem: {
    width: "100%",
    height: "100%",
    display: "flex",
    flexDirection: "row",
    backgroundColor: "#f2f4f5",
    marginBottom: 20,
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
  containerbutton: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
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
