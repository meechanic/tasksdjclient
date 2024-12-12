# coding: utf-8

"""
    TasksDJ API

    TasksDJ API  # noqa: E501

    OpenAPI spec version: v1
    Contact: meechanic.design@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from tasksdjclient.configuration import Configuration


class TaskTag(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'key': 'str',
        'value': 'str',
        'task': 'int'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'value': 'value',
        'task': 'task'
    }

    def __init__(self, id=None, key=None, value=None, task=None, _configuration=None):  # noqa: E501
        """TaskTag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._value = None
        self._task = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.key = key
        self.value = value
        self.task = task

    @property
    def id(self):
        """Gets the id of this TaskTag.  # noqa: E501


        :return: The id of this TaskTag.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskTag.


        :param id: The id of this TaskTag.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this TaskTag.  # noqa: E501


        :return: The key of this TaskTag.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TaskTag.


        :param key: The key of this TaskTag.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                key is not None and len(key) < 1):
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this TaskTag.  # noqa: E501


        :return: The value of this TaskTag.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TaskTag.


        :param value: The value of this TaskTag.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def task(self):
        """Gets the task of this TaskTag.  # noqa: E501


        :return: The task of this TaskTag.  # noqa: E501
        :rtype: int
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this TaskTag.


        :param task: The task of this TaskTag.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and task is None:
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501

        self._task = task

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TaskTag, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskTag):
            return True

        return self.to_dict() != other.to_dict()
