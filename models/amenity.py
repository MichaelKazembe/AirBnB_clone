#!/usr/bin/python3
"""defining amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity inherting from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """overriding"""
        super().__init__(*args, **kwargs)
