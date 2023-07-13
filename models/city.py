#!/usr/bin/python3
"""defining city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """overriding"""
        super().__init__(*args, **kwargs)
