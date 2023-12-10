#!/bin/bash/python3
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

"""
serialization and deserialization module
"""


class FileStorage:
    "container of serialization deserializtion methods"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        "returns the dictionary __objects"
        return FileStorage.__objects

    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        FileStorage.__objects[
            "{}.{}".format(
                obj.__class__.__name__,
                obj.id,
            )
        ] = obj

    def save(self):
        """
        method for serializing dictionary __objects to json string
        and save it to a file
        """
        dic = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            for key, value in FileStorage.__objects.items():
                dic[key] = value.to_dict()
            json.dump(dic, file)

    def reload(self):
        """
        method for deserializing json string to dictionary __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                content = file.read()
                if content:
                    dic = json.loads(content)
                    for key, value in dic.items():
                        self.new(eval(value["__class__"])(**value))
        except FileNotFoundError:
            pass
