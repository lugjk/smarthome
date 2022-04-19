import os
import flask
import datetime

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return '''<Text> API for Project </Text>'''

@app.route("/switch/data", methods = ["GET"])
def getData():
    SITEROOT = os.path.realpath(os.path.dirname(__file__))
    jsonUrl = os.path.join(SITEROOT, "data", "switch.json")
    switch = flask.json.load(open(jsonUrl, "r", encoding="utf8"))
    switch = [{"value": ele["value"], "time_created": ele["created_at"]} for ele in switch]
    return flask.jsonify(switch)

@app.route("/switch/processdata", methods = ["GET"])
def processData():
    SITEROOT = os.path.realpath(os.path.dirname(__file__))
    jsonUrl = os.path.join(SITEROOT, "data", "switch.json")
    switch = flask.json.load(open(jsonUrl, "r", encoding="utf8"))
    switch = [{"value": ele["value"], "time_created": ele["created_at"]} for ele in switch]
    # datetime_now = str(datetime.datetime.now())[:10]
    datetime_now = "2022-04-04"
    data = [ele for ele in switch if ele["time_created"][:10] == datetime_now]
    data = data[::-1]
    length_data = len(data)
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    labels = ["0", "6", "12", "18", "24"]
    stat_time_used = [0]*5
    time = 0
    j = 0
    first_flag = True
    for index, value in enumerate(labels):
        while (int(data[j]["time_created"][11:13]) < int(value)):
            if (data[j]["value"] == 1):
                time_start = datetime.datetime.strptime(data[j]["time_created"], date_format)
                m = 1
                while ((j + m) < length_data and data[j + m]["value"] == 1):
                    m += 1
                time_end = datetime.datetime.strptime(data[j + m]["time_created"], date_format)
                if first_flag:
                    time = time_end - time_start
                    first_flag = False
                else:
                    time += time_end - time_start
                j += m
            else:
                j += 1
        stat_time_used[index] = time
    return stat_time_used
                
if __name__ == "__main__":
    app.run(debug=True)