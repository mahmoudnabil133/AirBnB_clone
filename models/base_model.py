#!/usr/bin/python3
"""
Class: BaseModel that defines all common attributes/methods for other classes
Public instance attributes:
    id, created_at, updated_at
__str__: prints the string representation of the BaseModel
    ex: [<class name>] (<self.id>) <self.__dict__>
public instance methods:
    save(self): updates the public instance attribute updated_at
        with the current datetime
    to_dict(self): returns a dictionary containing all keys/values
        of __dict__ of the instance
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Prints the string representation of the BaseModel
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__,
        )

    def save(self):
        """
        Update the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        map = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                map[key] = value.isoformat()
            else:
                map[key] = value
            map["__class__"] = self.__class__.__name__
            return map
