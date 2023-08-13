#!/usr/bin/python3
"""Defining the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class reprensenting review.
    """

    place_id = ""
    user_id = ""
    text = ""
