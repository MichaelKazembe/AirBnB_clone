#!/usr/bin/python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel instance"""
        if kwargs is not None and kwargs != {}:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """returns string representation"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """dictionary representation of __dict__ of instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
