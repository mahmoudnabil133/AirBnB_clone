#!/usr/bin/python3
"""
review.py - class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
