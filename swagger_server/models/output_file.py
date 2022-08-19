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
from swagger_server.models.par_file import ParFile
from swagger_server import util


class OutputFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, file: ParFile=None, name: str=None):  # noqa: E501
        """OutputFile - a model defined in Swagger

        :param description: The description of this OutputFile.  # noqa: E501
        :type description: str
        :param file: The file of this OutputFile.  # noqa: E501
        :type file: ParFile
        :param name: The name of this OutputFile.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'description': str,
            'file': ParFile,
            'name': str
        }

        self.attribute_map = {
            'description': 'description',
            'file': 'file',
            'name': 'name'
        }

        self._description = description
        self._file = file
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'OutputFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OutputFile of this OutputFile.  # noqa: E501
        :rtype: OutputFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this OutputFile.


        :return: The description of this OutputFile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this OutputFile.


        :param description: The description of this OutputFile.
        :type description: str
        """

        self._description = description

    @property
    def file(self) -> ParFile:
        """Gets the file of this OutputFile.


        :return: The file of this OutputFile.
        :rtype: ParFile
        """
        return self._file

    @file.setter
    def file(self, file: ParFile):
        """Sets the file of this OutputFile.


        :param file: The file of this OutputFile.
        :type file: ParFile
        """

        self._file = file

    @property
    def name(self) -> str:
        """Gets the name of this OutputFile.


        :return: The name of this OutputFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this OutputFile.


        :param name: The name of this OutputFile.
        :type name: str
        """

        self._name = name
