# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.27-pipeline-namespace
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiCredential(object):
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
        'id': 'str',
        'created_at': 'datetime',
        'pipeline_id': 'str',
        'project_id': 'str',
        'api_key': 'str',
        'data_assets': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'pipeline_id': 'pipeline_id',
        'project_id': 'project_id',
        'api_key': 'api_key',
        'data_assets': 'data_assets'
    }

    def __init__(self, id=None, created_at=None, pipeline_id=None, project_id=None, api_key=None, data_assets=None):  # noqa: E501
        """ApiCredential - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._pipeline_id = None
        self._project_id = None
        self._api_key = None
        self._data_assets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        self.pipeline_id = pipeline_id
        self.project_id = project_id
        if api_key is not None:
            self.api_key = api_key
        if data_assets is not None:
            self.data_assets = data_assets

    @property
    def id(self):
        """Gets the id of this ApiCredential.  # noqa: E501


        :return: The id of this ApiCredential.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiCredential.


        :param id: The id of this ApiCredential.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this ApiCredential.  # noqa: E501


        :return: The created_at of this ApiCredential.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiCredential.


        :param created_at: The created_at of this ApiCredential.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this ApiCredential.  # noqa: E501


        :return: The pipeline_id of this ApiCredential.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this ApiCredential.


        :param pipeline_id: The pipeline_id of this ApiCredential.  # noqa: E501
        :type: str
        """
        if pipeline_id is None:
            raise ValueError("Invalid value for `pipeline_id`, must not be `None`")  # noqa: E501

        self._pipeline_id = pipeline_id

    @property
    def project_id(self):
        """Gets the project_id of this ApiCredential.  # noqa: E501


        :return: The project_id of this ApiCredential.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ApiCredential.


        :param project_id: The project_id of this ApiCredential.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def api_key(self):
        """Gets the api_key of this ApiCredential.  # noqa: E501

        TODO: what is the api_key  # noqa: E501

        :return: The api_key of this ApiCredential.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ApiCredential.

        TODO: what is the api_key  # noqa: E501

        :param api_key: The api_key of this ApiCredential.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def data_assets(self):
        """Gets the data_assets of this ApiCredential.  # noqa: E501

        List of data asset IDs  # noqa: E501

        :return: The data_assets of this ApiCredential.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_assets

    @data_assets.setter
    def data_assets(self, data_assets):
        """Sets the data_assets of this ApiCredential.

        List of data asset IDs  # noqa: E501

        :param data_assets: The data_assets of this ApiCredential.  # noqa: E501
        :type: list[str]
        """

        self._data_assets = data_assets

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
        if issubclass(ApiCredential, dict):
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
        if not isinstance(other, ApiCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
