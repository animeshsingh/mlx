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

from swagger_client.models.api_pipeline_task_arguments import ApiPipelineTaskArguments  # noqa: F401,E501


class ApiPipelineTask(object):
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
        'name': 'str',
        'artifact_type': 'str',
        'artifact_id': 'str',
        'arguments': 'ApiPipelineTaskArguments',
        'dependencies': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'artifact_type': 'artifact_type',
        'artifact_id': 'artifact_id',
        'arguments': 'arguments',
        'dependencies': 'dependencies'
    }

    def __init__(self, name=None, artifact_type=None, artifact_id=None, arguments=None, dependencies=None):  # noqa: E501
        """ApiPipelineTask - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._artifact_type = None
        self._artifact_id = None
        self._arguments = None
        self._dependencies = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.artifact_type = artifact_type
        self.artifact_id = artifact_id
        if arguments is not None:
            self.arguments = arguments
        if dependencies is not None:
            self.dependencies = dependencies

    @property
    def name(self):
        """Gets the name of this ApiPipelineTask.  # noqa: E501


        :return: The name of this ApiPipelineTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPipelineTask.


        :param name: The name of this ApiPipelineTask.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def artifact_type(self):
        """Gets the artifact_type of this ApiPipelineTask.  # noqa: E501

        The type of artifact for this task, can be either one of: 'component', 'model', 'notebook', 'pipeline'  # noqa: E501

        :return: The artifact_type of this ApiPipelineTask.  # noqa: E501
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """Sets the artifact_type of this ApiPipelineTask.

        The type of artifact for this task, can be either one of: 'component', 'model', 'notebook', 'pipeline'  # noqa: E501

        :param artifact_type: The artifact_type of this ApiPipelineTask.  # noqa: E501
        :type: str
        """
        if artifact_type is None:
            raise ValueError("Invalid value for `artifact_type`, must not be `None`")  # noqa: E501

        self._artifact_type = artifact_type

    @property
    def artifact_id(self):
        """Gets the artifact_id of this ApiPipelineTask.  # noqa: E501

        The UUID of the artifact for this task  # noqa: E501

        :return: The artifact_id of this ApiPipelineTask.  # noqa: E501
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """Sets the artifact_id of this ApiPipelineTask.

        The UUID of the artifact for this task  # noqa: E501

        :param artifact_id: The artifact_id of this ApiPipelineTask.  # noqa: E501
        :type: str
        """
        if artifact_id is None:
            raise ValueError("Invalid value for `artifact_id`, must not be `None`")  # noqa: E501

        self._artifact_id = artifact_id

    @property
    def arguments(self):
        """Gets the arguments of this ApiPipelineTask.  # noqa: E501


        :return: The arguments of this ApiPipelineTask.  # noqa: E501
        :rtype: ApiPipelineTaskArguments
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this ApiPipelineTask.


        :param arguments: The arguments of this ApiPipelineTask.  # noqa: E501
        :type: ApiPipelineTaskArguments
        """

        self._arguments = arguments

    @property
    def dependencies(self):
        """Gets the dependencies of this ApiPipelineTask.  # noqa: E501

        Task dependencies, referring to upstream tasks that have to be completed prior to running this task by their respective task names  # noqa: E501

        :return: The dependencies of this ApiPipelineTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this ApiPipelineTask.

        Task dependencies, referring to upstream tasks that have to be completed prior to running this task by their respective task names  # noqa: E501

        :param dependencies: The dependencies of this ApiPipelineTask.  # noqa: E501
        :type: list[str]
        """

        self._dependencies = dependencies

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
        if issubclass(ApiPipelineTask, dict):
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
        if not isinstance(other, ApiPipelineTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
