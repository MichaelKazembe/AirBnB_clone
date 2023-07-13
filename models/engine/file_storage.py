#!/usr/bin/python3
"""defining file_storage module"""
import json
import os


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all stores basemodel objects"""
        return self.__objects

    def new(self, obj):
        """adding new object to objects dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """save objects dictionary to file"""
        with open(self.__file_path, 'w') as f:
            diction = {key: value.to_dict() for key, value
                       in self.__objects.items()}
            json.dump(diction, f)

    def reload(self):
        """deserialize JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                diction = json.load(f)
                diction = {key: self.classes()[value["__class__"]]
                           (**value) for key, value in diction.items()}
                FileStorage.__objects = diction
        except FileNotFoundError:
            return

    def classes(self):
        """dictionary containging key/value pairs of classes"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "Amenity": Amenity,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "State": State,
                   "User": User}
        return classes
