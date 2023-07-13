#!/usr/bin/python3
"""defining state module"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherting from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """override"""
        super().__init__(*args, **kwargs)
