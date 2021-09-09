# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ProvenanceInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, provenance_description: str=None, provenance_name: str=None, provenance_source_date: str=None, provenance_source_id: str=None, provenance_source_namespace: str=None):  # noqa: E501
        """ProvenanceInformation - a model defined in Swagger

        :param provenance_description: The provenance_description of this ProvenanceInformation.  # noqa: E501
        :type provenance_description: str
        :param provenance_name: The provenance_name of this ProvenanceInformation.  # noqa: E501
        :type provenance_name: str
        :param provenance_source_date: The provenance_source_date of this ProvenanceInformation.  # noqa: E501
        :type provenance_source_date: str
        :param provenance_source_id: The provenance_source_id of this ProvenanceInformation.  # noqa: E501
        :type provenance_source_id: str
        :param provenance_source_namespace: The provenance_source_namespace of this ProvenanceInformation.  # noqa: E501
        :type provenance_source_namespace: str
        """
        self.swagger_types = {
            'provenance_description': str,
            'provenance_name': str,
            'provenance_source_date': str,
            'provenance_source_id': str,
            'provenance_source_namespace': str
        }

        self.attribute_map = {
            'provenance_description': 'provenanceDescription',
            'provenance_name': 'provenanceName',
            'provenance_source_date': 'provenanceSourceDate',
            'provenance_source_id': 'provenanceSourceId',
            'provenance_source_namespace': 'provenanceSourceNamespace'
        }

        self._provenance_description = provenance_description
        self._provenance_name = provenance_name
        self._provenance_source_date = provenance_source_date
        self._provenance_source_id = provenance_source_id
        self._provenance_source_namespace = provenance_source_namespace

    @classmethod
    def from_dict(cls, dikt) -> 'ProvenanceInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProvenanceInformation of this ProvenanceInformation.  # noqa: E501
        :rtype: ProvenanceInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provenance_description(self) -> str:
        """Gets the provenance_description of this ProvenanceInformation.


        :return: The provenance_description of this ProvenanceInformation.
        :rtype: str
        """
        return self._provenance_description

    @provenance_description.setter
    def provenance_description(self, provenance_description: str):
        """Sets the provenance_description of this ProvenanceInformation.


        :param provenance_description: The provenance_description of this ProvenanceInformation.
        :type provenance_description: str
        """

        self._provenance_description = provenance_description

    @property
    def provenance_name(self) -> str:
        """Gets the provenance_name of this ProvenanceInformation.


        :return: The provenance_name of this ProvenanceInformation.
        :rtype: str
        """
        return self._provenance_name

    @provenance_name.setter
    def provenance_name(self, provenance_name: str):
        """Sets the provenance_name of this ProvenanceInformation.


        :param provenance_name: The provenance_name of this ProvenanceInformation.
        :type provenance_name: str
        """

        self._provenance_name = provenance_name

    @property
    def provenance_source_date(self) -> str:
        """Gets the provenance_source_date of this ProvenanceInformation.


        :return: The provenance_source_date of this ProvenanceInformation.
        :rtype: str
        """
        return self._provenance_source_date

    @provenance_source_date.setter
    def provenance_source_date(self, provenance_source_date: str):
        """Sets the provenance_source_date of this ProvenanceInformation.


        :param provenance_source_date: The provenance_source_date of this ProvenanceInformation.
        :type provenance_source_date: str
        """

        self._provenance_source_date = provenance_source_date

    @property
    def provenance_source_id(self) -> str:
        """Gets the provenance_source_id of this ProvenanceInformation.


        :return: The provenance_source_id of this ProvenanceInformation.
        :rtype: str
        """
        return self._provenance_source_id

    @provenance_source_id.setter
    def provenance_source_id(self, provenance_source_id: str):
        """Sets the provenance_source_id of this ProvenanceInformation.


        :param provenance_source_id: The provenance_source_id of this ProvenanceInformation.
        :type provenance_source_id: str
        """

        self._provenance_source_id = provenance_source_id

    @property
    def provenance_source_namespace(self) -> str:
        """Gets the provenance_source_namespace of this ProvenanceInformation.


        :return: The provenance_source_namespace of this ProvenanceInformation.
        :rtype: str
        """
        return self._provenance_source_namespace

    @provenance_source_namespace.setter
    def provenance_source_namespace(self, provenance_source_namespace: str):
        """Sets the provenance_source_namespace of this ProvenanceInformation.


        :param provenance_source_namespace: The provenance_source_namespace of this ProvenanceInformation.
        :type provenance_source_namespace: str
        """

        self._provenance_source_namespace = provenance_source_namespace