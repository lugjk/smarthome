"""Application Models"""
import bson
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta, datetime

DATABASE_URL = 'mongodb://localhost:27017/'
client = MongoClient(DATABASE_URL)
db = client.Smarthome
DATEFORMAT = "%Y-%m-%dT%H:%M:%SZ"

class Devices:
    """Devices Model"""
    def __init__(self):
        return

    def create(self, name="", code="", category="", user_id=""):
        """Create a new device"""
        device = self.get_by_user_id_and_code(user_id, name)
        if device:
            return
        new_device = db.Devices.insert_one(
            {
                "name": name,
                "code": code,
                "category": category,
                "user_id": user_id
            }
        )
        return self.get_by_id(new_device.inserted_id)

    def get_all(self):
        """Get all devices"""
        devices = db.Devices.find()
        return [{**device, "_id": str(device["_id"])} for device in devices]

    def get_by_id(self, device_id):
        """Get a device by id"""
        device = db.Devices.find_one({"_id": bson.ObjectId(device_id)})
        if not device:
            return
        device["_id"] = str(device["_id"])
        return device

    def get_by_code(self, device_code):
        """Get a device by code"""
        device = db.Devices.find_one({"code": device_code})
        if not device:
            return
        device["_id"] = str(device["_id"])
        return device

    def get_by_user_id(self, user_id):
        """Get all devices created by a user"""
        devices = db.Devices.find({"user_id": user_id})
        return [{**device, "_id": str(device["_id"])} for device in devices]

    def get_by_user_id_and_code(self, user_id, code):
        """Get a devices given its code and id"""
        device = db.Devices.find_one({"user_id": user_id, "code": code})
        if not device:
            return
        device["_id"] = str(device["_id"])
        return device

    def get_by_category(self, category):
        """Get all devices by category"""
        devices = db.Devices.find({"category": category})
        return [device for device in devices]

    def get_by_user_id_and_category(self, user_id, category):
        """Get all devices by category for a particular user"""
        devices = db.Devices.find({"user_id": user_id, "category": category})
        return [{**device, "_id": str(device["_id"])} for device in devices]

    def update(self, device_id, name="" ,code="", category=""):
        """Update a device"""
        data={}
        if name: data["name"]=name
        if code: data["code"]=code
        if category: data["category"]=category

        device = db.Devices.update_one(
            {"_id": bson.ObjectId(device_id)},
            {
                "$set": data
            }
        )
        device = self.get_by_id(device_id)
        return device

    def delete(self, device_id):
        """Delete a device"""
        db.TimeUsed.delete_many({"Sensor": device_id})
        device = db.Devices.delete_one({"_id": bson.ObjectId(device_id)})
        return device

    def delete_by_user_id(self, user_id):
        """Delete all devices created by a user"""
        device = db.Devices.delete_many({"user_id": user_id})
        return device
    
    def get_timeused_by_id(self, device_id, time_start, time_end):
        """Get time used of device from time_start to time_end"""
        data = db.TimeUsed.find({
                        "Sensor": device_id,
                        "Timestamp": {
                            "$gt": datetime.strptime(time_start, DATEFORMAT),
                            "$lte": datetime.strptime(time_end, DATEFORMAT)
                        }
                    })
        total = timedelta()
        for d in data:
            d = datetime.strptime(d["Value"], "%H:%M:%S")
            total += timedelta(hours=d.hour, minutes=d.minute, seconds=d.second)
        return total.seconds/60/60

    def get_timeused_of_week(self, device_id):
        now = datetime.now().date()
        weekday = now.weekday()
        # twohour = timedelta(hours=2)
        return [self.get_timeused_by_id(device_id, (now-(weekday-i)*timedelta(1)).strftime(DATEFORMAT), (now-(weekday-i-1)*timedelta(1)).strftime(DATEFORMAT)) for i in range(1,8)]

class Rooms:
    """Rooms Model"""
    def __init__(self):
        return

    def create(self, name="", user_id=""):
        """Create a new room"""
        room = self.get_by_user_id_and_name(user_id, name)
        if room:
            return
        new_room = db.Rooms.insert_one(
            {
                "name": name,
                "user_id": user_id,
                "devices": []
            }
        )
        return self.get_by_id(new_room.inserted_id)

    def get_all(self):
        """Get all rooms"""
        rooms = db.Rooms.find()
        return [{**room, "_id": str(room["_id"])} for room in rooms]

    def get_by_id(self, room_id):
        """Get a room by id"""
        room = db.Rooms.find_one({"_id": bson.ObjectId(room_id)})
        if not room:
            return
        room["_id"] = str(room["_id"])
        return room

    def get_by_user_id(self, user_id):
        """Get all rooms created by a user"""
        rooms = db.Rooms.find({"user_id": user_id})
        return [{**room, "_id": str(room["_id"])} for room in rooms]

    def get_by_user_id_and_name(self, user_id, name):
        """Get a rooms given its name and id"""
        room = db.Rooms.find_one({"user_id": user_id, "name": name})
        if not room:
            return
        room["_id"] = str(room["_id"])
        room["devices"] = [Devices().get_by_id(d) for d in room["devices"]]
        return room

    def update(self, room_id, name="", devices=None):
        """Update a room"""
        data={}
        if name: data["name"]=name
        if devices != None: data["devices"]=devices

        room = db.Rooms.update_one(
            {"_id": bson.ObjectId(room_id)},
            {
                "$set": data
            }
        )
        room = self.get_by_id(room_id)
        return room

    def addDevice(self, room_id, device_id):
        """Add a device to room"""
        data=self.get_by_id(room_id)
        data["devices"].append(device_id)
        del data["_id"]

        room = db.Rooms.update_one(
            {"_id": bson.ObjectId(room_id)},
            {
                "$set": data
            }
        )
        room = self.get_by_id(room_id)
        return room

    def deleteDevice(self, room_id, device_id):
        """Add a device to room"""
        data=self.get_by_id(room_id)
        data["devices"].remove(device_id)
        del data["_id"]

        room = db.Rooms.update_one(
            {"_id": bson.ObjectId(room_id)},
            {
                "$set": data
            }
        )
        room = self.get_by_id(room_id)
        return room

    def delete(self, room_id):
        """Delete a room"""
        room = db.Rooms.delete_one({"_id": bson.ObjectId(room_id)})
        return room

    def delete_by_user_id(self, user_id):
        """Delete all rooms created by a user"""
        room = db.Rooms.delete_many({"user_id": user_id})
        return room
    

class User:
    """User Model"""
    def __init__(self):
        return

    def create(self, name="", email="", password=""):
        """Create a new user"""
        user = self.get_by_username(email)
        if user:
            return
        new_user = db.Account.insert_one(
            {
                "name": name,
                "email": email,
                "password": self.encrypt_password(password),
                "active": True
            }
        )
        return self.get_by_id(new_user.inserted_id)

    def get_all(self):
        """Get all users"""
        users = db.Account.find({"active": True})
        return [{**user, "_id": str(user["_id"])} for user in users]

    def get_by_id(self, user_id):
        """Get a user by id"""
        user = db.Account.find_one({"_id": bson.ObjectId(user_id), "active": True})
        if not user:
            return
        user["_id"] = str(user["_id"])
        return user

    def get_by_username(self, name):
        """Get a user by name"""
        user = db.Account.find_one({"name": name, "active": True})
        if not user:
            return
        user["_id"] = str(user["_id"])
        return user

    def changePassword(self, user_id, password="", newpassword=""):
        """Update a user"""
        user = self.get_by_id(user_id)
        if not user or not check_password_hash(user["password"], password):
            return

        data = {}
        data["password"] = self.encrypt_password(newpassword)

        user = db.Account.update_one(
            {"_id": bson.ObjectId(user_id)},
            {
                "$set": data
            }
        )
        user = self.get_by_id(user_id)
        return user

    def delete(self, user_id):
        """Delete a user"""
        Devices().delete_by_user_id(user_id)
        user = db.Account.delete_one({"_id": bson.ObjectId(user_id)})
        user = self.get_by_id(user_id)
        return user

    def disable_account(self, user_id):
        """Disable a user account"""
        user = db.Account.update_one(
            {"_id": bson.ObjectId(user_id)},
            {"$set": {"active": False}}
        )
        user = self.get_by_id(user_id)
        return user

    def encrypt_password(self, password):
        """Encrypt password"""
        return generate_password_hash(password)

    def login(self, name, password):
        """Login a user"""
        user = self.get_by_username(name)
        if not user or not check_password_hash(user["password"], password):
            return
        user.pop("password")
        return user
    