#!/bin/bash/python3
from models.base_model import BaseModel
import json
"""
serialization and deserialization module
"""


class FileStorage():
    "container of serialization deserializtion methods"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        "return a private class attribute __objects"
        return FileStorage.__objects

    def new(self, obj):
        "sets obj as a value of key --> class_name.id "
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        method of serialization ,before that we will
        convert the objects --> (wich are values of __objects dictionary)
        into dictionary ds by method to_dict from BaseModel class
        """
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()

        "now dic{} is ready to be dumped then stored to json file"
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(dic))

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
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                "handle if file is empty"
                if file.read():
                    obj = json.loads(file.read())
                    for key, value in obj.items():
                        FileStorage.__objects[key] = \
                            eval(value['__class__'])(**value)

        except FileNotFoundError:
            "handle when the file not exist"
            pass
