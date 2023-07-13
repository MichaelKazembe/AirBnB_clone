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
        with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
            diction = json.load(f)
            diction = {key: self.classes()[value["__class__"]]
                       (**value) for key, value in diction.items()}
            FileStorage.__objects = diction
