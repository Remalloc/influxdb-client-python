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


class LogicalExpression(Expression):
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
        'operator': 'str',
        'left': 'Expression',
        'right': 'Expression'
    }

    attribute_map = {
        'type': 'type',
        'operator': 'operator',
        'left': 'left',
        'right': 'right'
    }

    def __init__(self, type=None, operator=None, left=None, right=None):  # noqa: E501,D401,D403
        """LogicalExpression - a model defined in OpenAPI."""  # noqa: E501
        Expression.__init__(self)  # noqa: E501

        self._type = None
        self._operator = None
        self._left = None
        self._right = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if operator is not None:
            self.operator = operator
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

    @property
    def type(self):
        """Get the type of this LogicalExpression.

        Type of AST node

        :return: The type of this LogicalExpression.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this LogicalExpression.

        Type of AST node

        :param type: The type of this LogicalExpression.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def operator(self):
        """Get the operator of this LogicalExpression.

        :return: The operator of this LogicalExpression.
        :rtype: str
        """  # noqa: E501
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Set the operator of this LogicalExpression.

        :param operator: The operator of this LogicalExpression.
        :type: str
        """  # noqa: E501
        self._operator = operator

    @property
    def left(self):
        """Get the left of this LogicalExpression.

        :return: The left of this LogicalExpression.
        :rtype: Expression
        """  # noqa: E501
        return self._left

    @left.setter
    def left(self, left):
        """Set the left of this LogicalExpression.

        :param left: The left of this LogicalExpression.
        :type: Expression
        """  # noqa: E501
        self._left = left

    @property
    def right(self):
        """Get the right of this LogicalExpression.

        :return: The right of this LogicalExpression.
        :rtype: Expression
        """  # noqa: E501
        return self._right

    @right.setter
    def right(self, right):
        """Set the right of this LogicalExpression.

        :param right: The right of this LogicalExpression.
        :type: Expression
        """  # noqa: E501
        self._right = right

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
        if not isinstance(other, LogicalExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
