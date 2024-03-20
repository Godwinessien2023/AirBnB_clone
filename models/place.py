#!/usr/bin/python3
"""Place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class to inherit from BaseModel

       Attributes:
       city_id: City.id
       user_id: User.id
       name: empty string
       number_rooms: integer - 0
       number_bathrooms: integer - 0
       max_guest: integer - 0
       price_by_night: integer - 0
       latitude: float - 0.0
       longitude: float - 0.0
       amenity_ids: list of string
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []