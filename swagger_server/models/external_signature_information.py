# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ExternalSignatureInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, external_signature_id: str=None, external_signature_id_namespace: str=None, signature: str=None, signature_type: str=None):  # noqa: E501
        """ExternalSignatureInformation - a model defined in Swagger

        :param external_signature_id: The external_signature_id of this ExternalSignatureInformation.  # noqa: E501
        :type external_signature_id: str
        :param external_signature_id_namespace: The external_signature_id_namespace of this ExternalSignatureInformation.  # noqa: E501
        :type external_signature_id_namespace: str
        :param signature: The signature of this ExternalSignatureInformation.  # noqa: E501
        :type signature: str
        :param signature_type: The signature_type of this ExternalSignatureInformation.  # noqa: E501
        :type signature_type: str
        """
        self.swagger_types = {
            'external_signature_id': str,
            'external_signature_id_namespace': str,
            'signature': str,
            'signature_type': str
        }

        self.attribute_map = {
            'external_signature_id': 'externalSignatureId',
            'external_signature_id_namespace': 'externalSignatureIdNamespace',
            'signature': 'signature',
            'signature_type': 'signatureType'
        }

        self._external_signature_id = external_signature_id
        self._external_signature_id_namespace = external_signature_id_namespace
        self._signature = signature
        self._signature_type = signature_type

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalSignatureInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalSignatureInformation of this ExternalSignatureInformation.  # noqa: E501
        :rtype: ExternalSignatureInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def external_signature_id(self) -> str:
        """Gets the external_signature_id of this ExternalSignatureInformation.


        :return: The external_signature_id of this ExternalSignatureInformation.
        :rtype: str
        """
        return self._external_signature_id

    @external_signature_id.setter
    def external_signature_id(self, external_signature_id: str):
        """Sets the external_signature_id of this ExternalSignatureInformation.


        :param external_signature_id: The external_signature_id of this ExternalSignatureInformation.
        :type external_signature_id: str
        """

        self._external_signature_id = external_signature_id

    @property
    def external_signature_id_namespace(self) -> str:
        """Gets the external_signature_id_namespace of this ExternalSignatureInformation.


        :return: The external_signature_id_namespace of this ExternalSignatureInformation.
        :rtype: str
        """
        return self._external_signature_id_namespace

    @external_signature_id_namespace.setter
    def external_signature_id_namespace(self, external_signature_id_namespace: str):
        """Sets the external_signature_id_namespace of this ExternalSignatureInformation.


        :param external_signature_id_namespace: The external_signature_id_namespace of this ExternalSignatureInformation.
        :type external_signature_id_namespace: str
        """

        self._external_signature_id_namespace = external_signature_id_namespace

    @property
    def signature(self) -> str:
        """Gets the signature of this ExternalSignatureInformation.


        :return: The signature of this ExternalSignatureInformation.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature: str):
        """Sets the signature of this ExternalSignatureInformation.


        :param signature: The signature of this ExternalSignatureInformation.
        :type signature: str
        """

        self._signature = signature

    @property
    def signature_type(self) -> str:
        """Gets the signature_type of this ExternalSignatureInformation.


        :return: The signature_type of this ExternalSignatureInformation.
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type: str):
        """Sets the signature_type of this ExternalSignatureInformation.


        :param signature_type: The signature_type of this ExternalSignatureInformation.
        :type signature_type: str
        """

        self._signature_type = signature_type
