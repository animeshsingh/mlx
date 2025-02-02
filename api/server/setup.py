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

import sys
from setuptools import setup, find_packages

NAME = "mlx-api"
VERSION = "0.1.27"  # 0.1.27-pipeline-namespace

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# TODO: use/parse requirements.txt and include requirements.txt in MANIFEST.in
REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="MLX Server API",
    author_email="",
    url="https://github.com/machine-learning-exchange/mlx",
    keywords=["Swagger", "MLX API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Machine Learning Exchange API
    """
)

