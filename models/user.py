#!/usr/bin/python3
from models.base_model import BaseModel

"""
user.py - class User that inherits from BaseModel
"""


class User(BaseModel):
    """creates a new user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
