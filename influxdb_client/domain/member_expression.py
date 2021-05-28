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
from influxdb_client.domain.expression import Expression


class MemberExpression(Expression):
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
        'object': 'Expression',
        '_property': 'PropertyKey'
    }

    attribute_map = {
        'type': 'type',
        'object': 'object',
        '_property': 'property'
    }

    def __init__(self, type=None, object=None, _property=None):  # noqa: E501,D401,D403
        """MemberExpression - a model defined in OpenAPI."""  # noqa: E501
        Expression.__init__(self)  # noqa: E501

        self._type = None
        self._object = None
        self.__property = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if object is not None:
            self.object = object
        if _property is not None:
            self._property = _property

    @property
    def type(self):
        """Get the type of this MemberExpression.

        Type of AST node

        :return: The type of this MemberExpression.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this MemberExpression.

        Type of AST node

        :param type: The type of this MemberExpression.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def object(self):
        """Get the object of this MemberExpression.

        :return: The object of this MemberExpression.
        :rtype: Expression
        """  # noqa: E501
        return self._object

    @object.setter
    def object(self, object):
        """Set the object of this MemberExpression.

        :param object: The object of this MemberExpression.
        :type: Expression
        """  # noqa: E501
        self._object = object

    @property
    def _property(self):
        """Get the _property of this MemberExpression.

        :return: The _property of this MemberExpression.
        :rtype: PropertyKey
        """  # noqa: E501
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Set the _property of this MemberExpression.

        :param _property: The _property of this MemberExpression.
        :type: PropertyKey
        """  # noqa: E501
        self.__property = _property

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
        if not isinstance(other, MemberExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
