#!/usr/bin/python3
""" A class that serializes instances to a JSON file and
deserializes JSON file to instances: """
import json


class FileStorage:
    """
    This class manages data storage and retrieval in JSON format.

    Private class attributes:
    - __file_path: The file path for JSON storage.
    - __objects: A dictionary to store objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
        A dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
        - obj: A dictionary representing the object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the current objects to the JSON file.
        """
        with open(FileStorage.__file_path, 'w') as json_file:
            obj_dict = {k: v.to_dict()
                        for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, json_file)

    def classes(self):
        """
        Returns a dictionary of valid classes and their references.
        """
        from models.base_model import BaseModel
        from models.user import User
        classes = {"BaseModel": BaseModel,
                   "User": User}
        return classes

    def reload(self):
        """
        Reloads objects from the JSON file.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass

    def get_file_path(self):
        """ A getter of the private class attribute file_path """
        return FileStorage.__file_path
