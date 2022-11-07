#!/usr/bin/python3
# coding: UTF-8
#
# PAR Consortium
# Copyright (C) 2020
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.par_identifier import ParIdentifier
from swagger_server import util


class PreservationActionType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: ParIdentifier=None, label: str=None, local_last_modified_date: str=None):  # noqa: E501
        """PreservationActionType - a model defined in Swagger

        :param id: The id of this PreservationActionType.  # noqa: E501
        :type id: ParIdentifier
        :param label: The label of this PreservationActionType.  # noqa: E501
        :type label: str
        :param local_last_modified_date: The local_last_modified_date of this PreservationActionType.  # noqa: E501
        :type local_last_modified_date: str
        """
        self.swagger_types = {
            'id': ParIdentifier,
            'label': str,
            'local_last_modified_date': str
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'local_last_modified_date': 'localLastModifiedDate'
        }

        self._id = id
        self._label = label
        self._local_last_modified_date = local_last_modified_date

    @classmethod
    def from_dict(cls, dikt) -> 'PreservationActionType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PreservationActionType of this PreservationActionType.  # noqa: E501
        :rtype: PreservationActionType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> ParIdentifier:
        """Gets the id of this PreservationActionType.


        :return: The id of this PreservationActionType.
        :rtype: ParIdentifier
        """
        return self._id

    @id.setter
    def id(self, id: ParIdentifier):
        """Sets the id of this PreservationActionType.


        :param id: The id of this PreservationActionType.
        :type id: ParIdentifier
        """

        self._id = id

    @property
    def label(self) -> str:
        """Gets the label of this PreservationActionType.


        :return: The label of this PreservationActionType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this PreservationActionType.


        :param label: The label of this PreservationActionType.
        :type label: str
        """

        self._label = label

    @property
    def local_last_modified_date(self) -> str:
        """Gets the local_last_modified_date of this PreservationActionType.


        :return: The local_last_modified_date of this PreservationActionType.
        :rtype: str
        """
        return self._local_last_modified_date

    @local_last_modified_date.setter
    def local_last_modified_date(self, local_last_modified_date: str):
        """Sets the local_last_modified_date of this PreservationActionType.


        :param local_last_modified_date: The local_last_modified_date of this PreservationActionType.
        :type local_last_modified_date: str
        """

        self._local_last_modified_date = local_last_modified_date
