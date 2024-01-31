# -*- coding: utf-8 -*-

"""
openweathermapapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from openweathermapapi.api_helper import APIHelper


class Clouds(object):

    """Implementation of the 'Clouds' model.

    TODO: type model description here.

    Attributes:
        all (int): Cloudiness, %

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "all": 'all'
    }

    _optionals = [
        'all',
    ]

    def __init__(self,
                 all=APIHelper.SKIP):
        """Constructor for the Clouds class"""

        # Initialize members of the class
        if all is not APIHelper.SKIP:
            self.all = all 

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
        all = dictionary.get("all") if dictionary.get("all") else APIHelper.SKIP
        # Return an object of this model
        return cls(all)
