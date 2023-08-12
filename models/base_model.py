#!/usr/bin/python3
"""
This module contains the BaseModel which is the base
class for the AirBnb clone console.
"""
import uuid
import datetime
import time


class BaseModel:
    """
    A base class representing a generic model with common attributes
    and methods.

    Attributes:
        id (str): A unique identifier generated using UUID.
        created_at (datetime.datetime): The timestamp of object creation.
        updated_at (datetime.datetime): The timestamp of the last update.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance with a unique ID and
        creation timestamp. 'created_at' and 'updated_at' are initially
        set to the same timestamp.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")  # noqa
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")  # noqa
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' timestamp to the current time, indicating
        an update.
        """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object's attributes.

        Returns:
            dict: A dictionary containing object attributes and metadata.
        """
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = self.__class__.__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        return dict_cpy

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, ID, and attributes.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)  # noqa
