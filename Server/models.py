"""Application Models"""
import bson
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta, datetime

DATABASE_URL = 'mongodb://localhost:27017/'
client = MongoClient(DATABASE_URL)
db = client.Smarthome


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
        rooms = db.rooms.find()
        return [{**room, "_id": str(room["_id"])} for room in rooms]

    def get_by_id(self, room_id):
        """Get a room by id"""
        room = db.rooms.find_one({"_id": bson.ObjectId(room_id)})
        if not room:
            return
        room["_id"] = str(room["_id"])
        return room

    def get_by_user_id(self, user_id):
        """Get all rooms created by a user"""
        rooms = db.rooms.find({"user_id": user_id})
        return [{**room, "_id": str(room["_id"])} for room in rooms]

    def get_by_user_id_and_name(self, user_id, name):
        """Get a rooms given its name and id"""
        room = db.rooms.find_one({"user_id": user_id, "name": name})
        if not room:
            return
        room["_id"] = str(room["_id"])
        return room


    def update(self, room_id, name="", devices=None):
        """Update a room"""
        data={}
        if name: data["name"]=name
        if devices != None: data["devices"]=devices

        room = db.rooms.update_one(
            {"_id": bson.ObjectId(room_id)},
            {
                "$set": data
            }
        )
        room = self.get_by_id(room_id)
        return room

    def delete(self, room_id):
        """Delete a room"""
        room = db.rooms.delete_one({"_id": bson.ObjectId(room_id)})
        return room

    def delete_by_user_id(self, user_id):
        """Delete all rooms created by a user"""
        room = db.rooms.delete_many({"user_id": bson.ObjectId(user_id)})
        return room
    
class Devices:
    """Devices Model"""
    def __init__(self):
        return

    def create(self, name="", category="", user_id=""):
        """Create a new device"""
        device = self.get_by_user_id_and_name(user_id, name)
        if device:
            return
        new_device = db.Devices.insert_one(
            {
                "name": name,
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

    def get_by_name(self, device_name):
        """Get a device by name"""
        device = db.Devices.find_one({"name": device_name})
        if not device:
            return
        device["_id"] = str(device["_id"])
        return device

    def get_by_user_id(self, user_id):
        """Get all devices created by a user"""
        devices = db.Devices.find({"user_id": user_id})
        return [{**device, "_id": str(device["_id"])} for device in devices]

    def get_by_user_id_and_name(self, user_id, name):
        """Get a devices given its name and id"""
        device = db.Devices.find_one({"user_id": user_id, "name": name})
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

    def update(self, device_id, name="", category=""):
        """Update a device"""
        data={}
        if name: data["name"]=name
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
        device = db.Devices.delete_one({"_id": bson.ObjectId(device_id)})
        return device

    def delete_by_user_id(self, user_id):
        """Delete all devices created by a user"""
        device = db.Devices.delete_many({"user_id": bson.ObjectId(user_id)})
        return device
    
    def get_timeused_by_name(self, device_name, time_start, time_end):
        """Get time used of device from time_start to time_end"""
        print(device_name, datetime.strptime(time_start, "%Y-%m-%dT%H:%M:%SZ"), datetime.strptime(time_end, "%Y-%m-%dT%H:%M:%SZ"))
        data = db.TimeUsed.find({
                        "Sensor": device_name,
                        "Timestamp": {
                            "$gt": datetime.strptime(time_start, "%Y-%m-%dT%H:%M:%SZ"),
                            "$lte": datetime.strptime(time_end, "%Y-%m-%dT%H:%M:%SZ")
                        }
                    })
        total = timedelta()
        for d in data:
            d = datetime.strptime(d["Value"], "%H:%M:%S")
            total += timedelta(hours=d.hour, minutes=d.minute, seconds=d.second)
        return str(total)

class User:
    """User Model"""
    def __init__(self):
        return

    def create(self, name="", email="", password=""):
        """Create a new user"""
        user = self.get_by_email(email)
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
        user.pop("password")
        return user

    def get_by_email(self, email):
        """Get a user by email"""
        user = db.Account.find_one({"email": email, "active": True})
        if not user:
            return
        user["_id"] = str(user["_id"])
        return user

    def update(self, user_id, name="", email="", password=""):
        """Update a user"""
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email
        if password:
            data["password"] = self.encrypt_password(password)

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

    def login(self, email, password):
        """Login a user"""
        user = self.get_by_email(email)
        if not user or not check_password_hash(user["password"], password):
            return
        user.pop("password")
        return user