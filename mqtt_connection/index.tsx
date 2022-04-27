import * as mqtt from "mqtt/dist/mqtt"

const host = 'io.adafruit.com';
const port = 443;
const clientId = `mqtt_${Math.random().toString(16).slice(3)}`;

const connectUrl = `wss://${host}:${port}/mqtt`;
const mqtt_client = mqtt.connect(connectUrl, {
    clientId,
    clean: true,
    connectTimeout: 4000,
    username: 'Frost984',
    password: 'aio_zJfc62OsApbwxxiS4K4OjZCackUl',
    reconnectPeriod: 1000
});

const relay_feed = 'Frost984/feeds/group-project.bbc-relay';
const buzzer_feed = 'Frost984/feeds/group-project.bbc-buzzer';
const led_feed = 'Frost984/feeds/group-project.bbc-led';
const temp_feed = 'Frost984/feeds/group-project.bbc-temp';
const switch_feed = 'Frost984/feeds/group-project.bbc-switch';
const button_feed = 'Frost984/feeds/group-project.bbc-button';

const topics = [relay_feed, buzzer_feed, led_feed, temp_feed, switch_feed, button_feed]
var debug = false;
mqtt_client.on('connect', () => {
    if (debug) {console.log('Connected');}
    mqtt_client.subscribe(topics, () => {
        if (debug){console.log(`Subscribe to topic '${topics}'`);}
    })
});
var mqtt_callbacks = {};

var debug = false;
mqtt_client.on('message', (topic, payload) => {
    if (debug){
        console.log('Received Message:', topic, payload.toString())
    }
    if (topic in mqtt_callbacks) {mqtt_callbacks[topic](payload);}
    });

module.exports = {
    mqtt_client: mqtt_client,
    relay_feed: relay_feed,
    buzzer_feed: buzzer_feed,
    led_feed: led_feed,
    temp_feed: temp_feed,
    switch_feed: switch_feed,
    button_feed: button_feed,
    mqtt_callbacks: mqtt_callbacks
}
