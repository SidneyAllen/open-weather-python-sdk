# -*- coding: utf-8 -*-

"""
openweathermapapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from openweathermapapi.api_helper import APIHelper
from openweathermapapi.configuration import Server
from openweathermapapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from openweathermapapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from openweathermapapi.models.successful_response import SuccessfulResponse
from openweathermapapi.exceptions.api_exception import APIException


class CurrentWeatherDataController(BaseController):

    """A Controller to access Endpoints in the openweathermapapi API."""
    def __init__(self, config):
        super(CurrentWeatherDataController, self).__init__(config)

    def current_weather_data(self,
                             q=None):
        """Does a GET request to /weather.

        Get the current weather info

        Args:
            q (str, optional): For the query value, type the city name and
                optionally the country code divided by comma; use ISO 3166
                country codes.

        Returns:
            SuccessfulResponse: Response from the API. Successful response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/weather')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('q')
                         .value(q))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SuccessfulResponse.from_dictionary)
            .local_error('404', 'Not found response', APIException)
        ).execute()
