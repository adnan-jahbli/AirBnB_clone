#!/usr/bin/python3
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

    Methods:
        __init__: Initializes a BaseModel instance.
        save: Updates the 'updated_at' timestamp to the current time.
        to_dict: Returns a dictionary representation of the object's
        attributes.
        __str__: Returns a string representation of the object.
    """

    def __init__(self):
        """
        Initializes a BaseModel instance with a unique ID and
        creation timestamp. 'created_at' and 'updated_at' are initially
        set to the same timestamp.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Updates the 'updated_at' timestamp to the current time, indicating
        an update.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object's attributes.

        Returns:
            dict: A dictionary containing object attributes and metadata.
        """
        dict_cpy = self.__dict__
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
