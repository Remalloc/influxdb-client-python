# coding: utf-8

"""
Influx OSS API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb_client.domain.statement import Statement


class OptionStatement(Statement):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'assignment': 'object'
    }

    attribute_map = {
        'type': 'type',
        'assignment': 'assignment'
    }

    def __init__(self, type=None, assignment=None):  # noqa: E501,D401,D403
        """OptionStatement - a model defined in OpenAPI."""  # noqa: E501
        Statement.__init__(self)  # noqa: E501

        self._type = None
        self._assignment = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if assignment is not None:
            self.assignment = assignment

    @property
    def type(self):
        """Get the type of this OptionStatement.

        Type of AST node

        :return: The type of this OptionStatement.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this OptionStatement.

        Type of AST node

        :param type: The type of this OptionStatement.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def assignment(self):
        """Get the assignment of this OptionStatement.

        :return: The assignment of this OptionStatement.
        :rtype: object
        """  # noqa: E501
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        """Set the assignment of this OptionStatement.

        :param assignment: The assignment of this OptionStatement.
        :type: object
        """  # noqa: E501
        self._assignment = assignment

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, OptionStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
