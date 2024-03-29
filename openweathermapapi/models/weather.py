# -*- coding: utf-8 -*-

"""
openweathermapapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from openweathermapapi.api_helper import APIHelper


class Weather(object):

    """Implementation of the 'Weather' model.

    TODO: type model description here.

    Attributes:
        id (int): Weather condition id
        main (str): Group of weather parameters (Rain, Snow, Extreme etc.)
        description (str): Weather condition within the group
        icon (str): Weather icon id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "main": 'main',
        "description": 'description',
        "icon": 'icon'
    }

    _optionals = [
        'id',
        'main',
        'description',
        'icon',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 main=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 icon=APIHelper.SKIP):
        """Constructor for the Weather class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if main is not APIHelper.SKIP:
            self.main = main 
        if description is not APIHelper.SKIP:
            self.description = description 
        if icon is not APIHelper.SKIP:
            self.icon = icon 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        main = dictionary.get("main") if dictionary.get("main") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        icon = dictionary.get("icon") if dictionary.get("icon") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   main,
                   description,
                   icon)
