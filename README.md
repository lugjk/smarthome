# Smarthome

## Getting started

#### Clone the repo
```
git clone https://github.com/lugjk/smarthome
cd smarthome
```

#### Install dependencies
For server machine and the gateway (in our demonstration, these 2 are actually 1 machine)
```
pip install -r requirements.txt
```

For client machine
```
yarn install
```

## Run the app:
There are some configurations to do before you can start running this app (like changing the server IP and the adafruit key, etc.) but those config are still kinda messy, so (maybe) I'll write the guide after we finish this shitty project.

On the server, run
```
python Server/app.py
```

For the client, we use Expo as our developing and testing platform. On the client machine, run
```
expo start
```

to start the app in testing mode, then use can follow the instructions on the screen to run the app on a phone or in a web browser.
(It would be so nice if we find out how to build a standalone APK. 2 days left, anyone?)

To start the gateway, first connect your board and load `gateway/full_script.py` to it. Then run
```
python gateway/main.py
```

to connect the gateway to the adafruit server.
