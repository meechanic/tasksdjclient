# coding: utf-8

"""
    TasksDJ API

    TasksDJ API  # noqa: E501

    OpenAPI spec version: v1
    Contact: meechanic.design@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import tasksdjclient
from tasksdjclient.api.task_tags_api import TaskTagsApi  # noqa: E501
from tasksdjclient.rest import ApiException


class TestTaskTagsApi(unittest.TestCase):
    """TaskTagsApi unit test stubs"""

    def setUp(self):
        self.api = tasksdjclient.api.task_tags_api.TaskTagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_task_tags_create(self):
        """Test case for task_tags_create

        """
        pass

    def test_task_tags_delete(self):
        """Test case for task_tags_delete

        """
        pass

    def test_task_tags_list(self):
        """Test case for task_tags_list

        """
        pass

    def test_task_tags_partial_update(self):
        """Test case for task_tags_partial_update

        """
        pass

    def test_task_tags_read(self):
        """Test case for task_tags_read

        """
        pass

    def test_task_tags_update(self):
        """Test case for task_tags_update

        """
        pass


if __name__ == '__main__':
    unittest.main()