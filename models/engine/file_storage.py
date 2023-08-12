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

    Public methods:
    - all(self): Returns the dictionary of all stored objects.
    - new(self, obj): Adds a new object to the storage dictionary.
    - save(self): Saves the current objects to the JSON file.
    - reload(self): Reloads objects from the JSON file.

    Example usage:
    ```
    storage = FileStorage()
    data = {"id": "123", "__class__": "Example"}
    storage.new(data)
    storage.save()
    storage.reload()
    all_objects = storage.all()
    ```
    """

    __file_path = "./file.json"  # Private attribute for JSON file path
    __objects = {}               # Private attribute to store objects

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
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """
        Reloads objects from the JSON file.
        """
        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects = json.load(json_file).copy()
        except FileNotFoundError:
            pass
