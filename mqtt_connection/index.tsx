// import * as mqtt from "mqtt";
import * as mqtt from "mqtt/dist/mqtt";

const host = "io.adafruit.com";
const port = 443;
const clientId = `mqtt_${Math.random().toString(16).slice(3)}`;

const connectUrl = `wss://${host}:${port}/mqtt`;
export const mqtt_client = mqtt.connect(connectUrl, {
  clientId,
  clean: true,
  connectTimeout: 4000,
  username: "Frost984",
  
  password: "",

  reconnectPeriod: 1000,
});

export const relay_feed = "Frost984/feeds/group-project.bbc-relay";
export const buzzer_feed = "Frost984/feeds/group-project.bbc-buzzer";
export const led_feed = "Frost984/feeds/group-project.bbc-led";
export const temp_feed = "Frost984/feeds/group-project.bbc-temp";
export const switch_feed = "Frost984/feeds/group-project.bbc-switch";
export const button_feed = "Frost984/feeds/group-project.bbc-button";

const topics = [
  relay_feed,
  buzzer_feed,
  led_feed,
  temp_feed,
  switch_feed,
  button_feed,
];
var debug = true;
mqtt_client.on("connect", () => {
  if (debug) {
    console.log("Connected");
  }
  mqtt_client.subscribe(topics, () => {
    if (debug) {
      console.log(`Subscribe to topic '${topics}'`);
    }
  });
});
export const mqtt_callbacks: { [key: string]: (number: number) => void } = {};

// var debug = true;
mqtt_client.on("message", (topic: string, payload: number) => {
  if (debug) {
    console.log("Received Message:", topic, payload.toString());
  }
  if (topic in mqtt_callbacks) {
    mqtt_callbacks[topic](payload);
  }
});

