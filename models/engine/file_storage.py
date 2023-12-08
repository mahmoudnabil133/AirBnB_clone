#!/bin/bash/python3
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os

"""
serialization and deserialization module
"""


class FileStorage:
    "container of serialization deserializtion methods"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        "return a private class attribute __objects"
        return FileStorage.__objects

    def new(self, obj):
        "sets obj as a value of key --> class_name.id"
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        method of serialization ,before that we will
        convert the objects --> (wich are values of __objects dictionary)
        into dictionary ds by method to_dict from BaseModel class
        """
        dic = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            for key, value in FileStorage.__objects.items():
                dic[key] = value.to_dict()
            json.dump(dic, file)

    def reload(self):
        """
        method for deserializing json string to dictionary
        dataStructure after that convert a dict into a obj by creating
        instance from the parent class,
        finally update the private class attribute __objects
        with assigning each
        obj to its key.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                dic = json.load(file)
                for key, value in dic.items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
            pass
        finally:
            pass
        pass
