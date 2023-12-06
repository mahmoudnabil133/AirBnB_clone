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
        Initialize the BaseModel class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Print the string representation of the BaseModel class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of
        s__dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
