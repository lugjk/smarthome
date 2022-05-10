import jwt, os
from flask import Flask, request, jsonify
from flask_cors import CORS
from multiprocessing import Process
from UpdateData import loopUpdate
# from validate import validate_device, validate_email_and_password, validate_user

app = Flask(__name__)
CORS(app)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY

from Models import Devices, User, Rooms
from Auth import token_required


@app.route("/", methods=["GET"])
def hello():
    return '''<Text> API for Project </Text>'''

@app.route("/users", methods=["POST"])
def add_user():
    try:
        user = request.json
        if not user:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        # is_validated = validate_user(**user)
        # if is_validated is not True:
        #     return dict(message='Invalid data', data=None, error=is_validated), 400
        user = User().create(**user)
        if not user:
            return {
                "message": "User already exists",
                "error": "Conflict",
                "data": None
            }, 409
        return {
            "message": "Successfully created new user",
            "data": user
        }, 201
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500

@app.route("/users/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        # validate input
        # is_validated = validate_email_and_password(data.get('email'), data.get('password'))
        # if is_validated is not True:
        #     return dict(message='Invalid data', data=None, error=is_validated), 400
        user = User().login(
            data["email"],
            data["password"]
        )
        if user:
            try:
                # token should expire after 24 hrs
                user["token"] = jwt.encode(
                    {"user_id": user["_id"]},
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
                return {
                    "message": "Successfully fetched auth token",
                    "data": user
                }
            except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 500
        return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }, 404
    except Exception as e:
        return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
        }, 500


@app.route("/users/", methods=["GET"])
@token_required
def get_current_user(current_user):
    return jsonify({
        "message": "successfully retrieved user profile",
        "data": current_user
    })

@app.route("/users/", methods=["PUT"])
@token_required
def update_user(current_user):
    try:
        user = request.json
        user = User().changePassword(current_user["_id"], user["password"], user["newpassword"])
        print(user)
        return jsonify({
            "message": "successfully updated account",
            "data": user
        }), 201
    except Exception as e:
        return jsonify({
            "message": "failed to update account",
            "error": str(e),
            "data": None
        }), 400

@app.route("/users/", methods=["DELETE"])
@token_required
def disable_user(current_user):
    try:
        User().disable_account(current_user["_id"])
        return jsonify({
            "message": "successfully disabled acount",
            "data": None
        }), 204
    except Exception as e:
        return jsonify({
            "message": "failed to disable account",
            "error": str(e),
            "data": None
        }), 400

@app.route("/devices", methods=["POST"])
@token_required
def add_device(current_user):
    try:
        device = dict(request.json)

        if not device:
            return {
                "message": "Invalid data, you need to give the device name device, catelogy, userID",
                "data": None,
                "error": "Bad Request"
            }, 400


        device["user_id"] = current_user["_id"]
        # is_validated = validate_device(**device)
        # if is_validated is not True:
        #     return {
        #         "message": "Invalid data",
        #         "data": None,
        #         "error": is_validated
        #     }, 400
        device = Devices().create(**device)
        if not device:
            return {
                "message": "The device has been created by user",
                "data": None,
                "error": "Conflict"
            }, 400
        return jsonify({
            "message": "successfully created a new device",
            "data": device
        }), 201
    except Exception as e:
        return jsonify({
            "message": "failed to create a new device",
            "error": str(e),
            "data": None
        }), 500

@app.route("/devices/", methods=["GET"])
@token_required
def get_devices(current_user):
    try:
        devices = Devices().get_by_user_id(current_user["_id"])
        return jsonify({
            "message": "successfully retrieved all devices",
            "data": devices
        })
    except Exception as e:
        return jsonify({
            "message": "failed to retrieve all devices",
            "error": str(e),
            "data": None
        }), 500

@app.route("/devices/<device_name>", methods=["GET"])
@token_required
def get_device(current_user, device_name):
    try:
        device = Devices().get_by_code(device_name)
        if not device or device["user_id"] != current_user["_id"]:
            return {
                "message": "device not found for user",
                "data": None,
                "error": "Not found"
            }, 404
        return jsonify({
            "message": "successfully retrieved a device",
            "data": device
        })
    except Exception as e:
        return jsonify({
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }), 500

@app.route("/devices/<device_name>", methods=["PUT"])
@token_required
def update_device(current_user, device_name):
    try:
        device = Devices().get_by_code(device_name)
        if not device or device["user_id"] != current_user["_id"]:
            return {
                "message": "device not found for user",
                "data": None,
                "error": "Not found"
            }, 404
        device = request.form

        device = Devices().update(device_name, **device)
        return jsonify({
            "message": "successfully updated a device",
            "data": device
        }), 201

    except Exception as e:
        return jsonify({
            "message": "failed to update a device",
            "error": str(e),
            "data": None
        }), 400

@app.route("/devices/<device_name>", methods=["DELETE"])
@token_required
def delete_device(current_user, device_name):
    try:
        device = Devices().get_by_code(device_name)
        if not device or device["user_id"] != current_user["_id"]:
            return {
                "message": "device not found for user",
                "data": None,
                "error": "Not found"
            }, 404
        Devices().delete(device_name)
        return jsonify({
            "message": "successfully deleted a device",
            "data": None
        }), 204
    except Exception as e:
        return jsonify({
            "message": "failed to delete a device",
            "error": str(e),
            "data": None
        }), 400


@app.route("/devices/data/<device_id>", methods=["GET"])
@token_required
def get_data_device(current_user, device_id):
    print(device_id)
    try:
        # device_id = request.json["_id"]
        device = Devices().get_by_id(device_id)
        if not device or device["user_id"] != current_user["_id"]:
            return {
                "message": "device not found for user",
                "data": None,
                "error": "Not Found"
            }, 404
        timeused = Devices().get_timeused_of_day(device_id)
        return jsonify({
            "message": "successfully retrieved a device",
            "data": timeused
        }), 201
    except Exception as e:
        return jsonify({
            "message": "failed to get timeused for device",
            "error": str(e),
            "data": None
        }), 500

@app.route("/rooms", methods=["POST"])
@token_required
def add_room(current_user):
    try:
        room = dict(request.json)

        if not room:
            return {
                "message": "Invalid data, you need to give the room name room, catelogy, userID",
                "data": None,
                "error": "Bad Request"
            }, 400

        room["user_id"] = current_user["_id"]

        room = Rooms().create(**room)
        if not room:
            return {
                "message": "The room has been created by user",
                "data": None,
                "error": "Conflict"
            }, 400
        return jsonify({
            "message": "successfully created a new room",
            "data": room
        }), 201

    except Exception as e:
        return jsonify({
            "message": "failed to create a new room",
            "error": str(e),
            "data": None
        }), 500

@app.route("/rooms/", methods=["GET"])
@token_required
def get_rooms(current_user):
    try:
        rooms = Rooms().get_by_user_id(current_user["_id"])
        return jsonify({
            "message": "successfully retrieved all rooms",
            "data": rooms
        })
    except Exception as e:
        return jsonify({
            "message": "failed to retrieve all rooms",
            "error": str(e),
            "data": None
        }), 500

@app.route("/rooms/<room_name>", methods=["GET"])
@token_required
def get_room(current_user, room_name):
    try:
        room = Rooms().get_by_user_id_and_name(current_user["_id"], room_name)
        if not room:
            return {
                "message": "room not found",
                "data": None,
                "error": "Not Found"
            }, 404
        return jsonify({
            "message": "successfully retrieved a room",
            "data": room
        })
    except Exception as e:
        return jsonify({
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }), 500

@app.route("/rooms/<room_name>", methods=["PUT"])
@token_required
def update_room(current_user, room_name):
    try:
        room = Rooms().get_by_user_id_and_name(current_user["_id"], room_name)
        if not room:
            return {
                "message": "room not found for user",
                "data": None,
                "error": "Not found"
            }, 404
        room = request.form

        room = Rooms().update(room_name, **room)
        return jsonify({
            "message": "successfully updated a room",
            "data": room
        }), 201
    except Exception as e:
        return jsonify({
            "message": "failed to update a room",
            "error": str(e),
            "data": None
        }), 400

@app.route("/rooms/<room_name>", methods=["DELETE"])
@token_required
def delete_room(current_user, room_name):
    try:
        room = Rooms().get_by_name(room_name)
        if not room or room["user_id"] != current_user["_id"]:
            return {
                "message": "room not found for user",
                "data": None,
                "error": "Not found"
            }, 404
        Rooms().delete(room_name)
        return jsonify({
            "message": "successfully deleted a room",
            "data": None
        }), 204
    except Exception as e:
        return jsonify({
            "message": "failed to delete a room",
            "error": str(e),
            "data": None
        }), 400

@app.errorhandler(403)
def forbidden(e):
    return jsonify({
        "message": "Forbidden",
        "error": str(e),
        "data": None
    }), 403

@app.errorhandler(404)
def forbidden(e):
    return jsonify({
        "message": "Endpoint Not Found",
        "error": str(e),
        "data": None
    }), 404


if __name__ == "__main__":
    Process(target=loopUpdate).start()
    app.run(debug=True)