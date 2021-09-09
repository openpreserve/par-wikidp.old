# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util
from swagger_server.models.par_property import ParProperty


class ParProperties(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, par_properties: List[ParProperty]=None):  # noqa: E501
        """ParProperties - a model defined in Swagger

        :param par_properties: The par_properties of this ParProperties.  # noqa: E501
        :type par_properties: List[ParProperty]
        """
        self.swagger_types = {
            'par_properties': List[ParProperty]
        }

        self.attribute_map = {
            'par_properties': 'parProperties'
        }

        self._par_properties = par_properties

    @classmethod
    def from_dict(cls, dikt) -> 'ParProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ParProperties of this ParProperties.  # noqa: E501
        :rtype: ParProperties
        """
        return util.deserialize_model(dikt, cls)

    @property
    def par_properties(self) -> List[ParProperty]:
        """Gets the par_properties of this ParProperties.


        :return: The par_properties of this ParProperties.
        :rtype: List[ParProperty]
        """
        return self._par_properties

    @par_properties.setter
    def par_properties(self, par_properties: List[ParProperty]):
        """Sets the par_properties of this ParProperties.


        :param par_properties: The par_properties of this ParProperties.
        :type par_properties: List[ParProperty]
        """

        self._par_properties = par_properties