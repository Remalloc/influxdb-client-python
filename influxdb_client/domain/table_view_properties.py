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
from influxdb_client.domain.view_properties import ViewProperties


class TableViewProperties(ViewProperties):
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
        'queries': 'list[DashboardQuery]',
        'colors': 'list[DashboardColor]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool',
        'table_options': 'TableViewPropertiesTableOptions',
        'field_options': 'list[RenamableField]',
        'time_format': 'str',
        'decimal_places': 'DecimalPlaces'
    }

    attribute_map = {
        'type': 'type',
        'queries': 'queries',
        'colors': 'colors',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty',
        'table_options': 'tableOptions',
        'field_options': 'fieldOptions',
        'time_format': 'timeFormat',
        'decimal_places': 'decimalPlaces'
    }

    def __init__(self, type=None, queries=None, colors=None, shape=None, note=None, show_note_when_empty=None, table_options=None, field_options=None, time_format=None, decimal_places=None):  # noqa: E501,D401,D403
        """TableViewProperties - a model defined in OpenAPI."""  # noqa: E501
        ViewProperties.__init__(self)  # noqa: E501

        self._type = None
        self._queries = None
        self._colors = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self._table_options = None
        self._field_options = None
        self._time_format = None
        self._decimal_places = None
        self.discriminator = None

        self.type = type
        self.queries = queries
        self.colors = colors
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty
        self.table_options = table_options
        self.field_options = field_options
        self.time_format = time_format
        self.decimal_places = decimal_places

    @property
    def type(self):
        """Get the type of this TableViewProperties.

        :return: The type of this TableViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this TableViewProperties.

        :param type: The type of this TableViewProperties.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def queries(self):
        """Get the queries of this TableViewProperties.

        :return: The queries of this TableViewProperties.
        :rtype: list[DashboardQuery]
        """  # noqa: E501
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Set the queries of this TableViewProperties.

        :param queries: The queries of this TableViewProperties.
        :type: list[DashboardQuery]
        """  # noqa: E501
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501
        self._queries = queries

    @property
    def colors(self):
        """Get the colors of this TableViewProperties.

        Colors define color encoding of data into a visualization

        :return: The colors of this TableViewProperties.
        :rtype: list[DashboardColor]
        """  # noqa: E501
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Set the colors of this TableViewProperties.

        Colors define color encoding of data into a visualization

        :param colors: The colors of this TableViewProperties.
        :type: list[DashboardColor]
        """  # noqa: E501
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501
        self._colors = colors

    @property
    def shape(self):
        """Get the shape of this TableViewProperties.

        :return: The shape of this TableViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Set the shape of this TableViewProperties.

        :param shape: The shape of this TableViewProperties.
        :type: str
        """  # noqa: E501
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501
        self._shape = shape

    @property
    def note(self):
        """Get the note of this TableViewProperties.

        :return: The note of this TableViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._note

    @note.setter
    def note(self, note):
        """Set the note of this TableViewProperties.

        :param note: The note of this TableViewProperties.
        :type: str
        """  # noqa: E501
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501
        self._note = note

    @property
    def show_note_when_empty(self):
        """Get the show_note_when_empty of this TableViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this TableViewProperties.
        :rtype: bool
        """  # noqa: E501
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Set the show_note_when_empty of this TableViewProperties.

        If true, will display note when empty

        :param show_note_when_empty: The show_note_when_empty of this TableViewProperties.
        :type: bool
        """  # noqa: E501
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501
        self._show_note_when_empty = show_note_when_empty

    @property
    def table_options(self):
        """Get the table_options of this TableViewProperties.

        :return: The table_options of this TableViewProperties.
        :rtype: TableViewPropertiesTableOptions
        """  # noqa: E501
        return self._table_options

    @table_options.setter
    def table_options(self, table_options):
        """Set the table_options of this TableViewProperties.

        :param table_options: The table_options of this TableViewProperties.
        :type: TableViewPropertiesTableOptions
        """  # noqa: E501
        if table_options is None:
            raise ValueError("Invalid value for `table_options`, must not be `None`")  # noqa: E501
        self._table_options = table_options

    @property
    def field_options(self):
        """Get the field_options of this TableViewProperties.

        fieldOptions represent the fields retrieved by the query with customization options

        :return: The field_options of this TableViewProperties.
        :rtype: list[RenamableField]
        """  # noqa: E501
        return self._field_options

    @field_options.setter
    def field_options(self, field_options):
        """Set the field_options of this TableViewProperties.

        fieldOptions represent the fields retrieved by the query with customization options

        :param field_options: The field_options of this TableViewProperties.
        :type: list[RenamableField]
        """  # noqa: E501
        if field_options is None:
            raise ValueError("Invalid value for `field_options`, must not be `None`")  # noqa: E501
        self._field_options = field_options

    @property
    def time_format(self):
        """Get the time_format of this TableViewProperties.

        timeFormat describes the display format for time values according to moment.js date formatting

        :return: The time_format of this TableViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Set the time_format of this TableViewProperties.

        timeFormat describes the display format for time values according to moment.js date formatting

        :param time_format: The time_format of this TableViewProperties.
        :type: str
        """  # noqa: E501
        if time_format is None:
            raise ValueError("Invalid value for `time_format`, must not be `None`")  # noqa: E501
        self._time_format = time_format

    @property
    def decimal_places(self):
        """Get the decimal_places of this TableViewProperties.

        :return: The decimal_places of this TableViewProperties.
        :rtype: DecimalPlaces
        """  # noqa: E501
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Set the decimal_places of this TableViewProperties.

        :param decimal_places: The decimal_places of this TableViewProperties.
        :type: DecimalPlaces
        """  # noqa: E501
        if decimal_places is None:
            raise ValueError("Invalid value for `decimal_places`, must not be `None`")  # noqa: E501
        self._decimal_places = decimal_places

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
        if not isinstance(other, TableViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
