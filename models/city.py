#!/usr/bin/python3
"""Defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class reprensenting the User city.
    """

    state_id = ""
    name = ""
