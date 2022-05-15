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
On the server, first you need to change Mongo DB URI in file Server/Models.py, then run:
```
python Server/app.py
```

For the client, you need to change the server IP (which show when you run server) in file config/url.js, then run:
```
expo start
```

to start the app in testing mode, then use can follow the instructions on the screen to run the app on a phone or in a web browser.

To start the gateway, first connect your board and load `gateway/full_script.py` to it and change Adafruit key in gateway/main.py. Then run
```
python gateway/main.py
```

to connect the gateway to the adafruit server.


Finally, we develop a desktop application that can manage customer information, you can run it by:
```
python admin/app.py
```