# tasksdjclient
TasksDJ API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import tasksdjclient 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tasksdjclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import tasksdjclient
from tasksdjclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = tasksdjclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tasksdjclient.ApiTokenAuthApi(tasksdjclient.ApiClient(configuration))
data = tasksdjclient.AuthToken() # AuthToken | 

try:
    api_response = api_instance.api_token_auth_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenAuthApi->api_token_auth_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiTokenAuthApi* | [**api_token_auth_create**](docs/ApiTokenAuthApi.md#api_token_auth_create) | **POST** /api-token-auth/ | 
*TaskTagsApi* | [**task_tags_create**](docs/TaskTagsApi.md#task_tags_create) | **POST** /task-tags/ | 
*TaskTagsApi* | [**task_tags_delete**](docs/TaskTagsApi.md#task_tags_delete) | **DELETE** /task-tags/{id}/ | 
*TaskTagsApi* | [**task_tags_list**](docs/TaskTagsApi.md#task_tags_list) | **GET** /task-tags/ | 
*TaskTagsApi* | [**task_tags_partial_update**](docs/TaskTagsApi.md#task_tags_partial_update) | **PATCH** /task-tags/{id}/ | 
*TaskTagsApi* | [**task_tags_read**](docs/TaskTagsApi.md#task_tags_read) | **GET** /task-tags/{id}/ | 
*TaskTagsApi* | [**task_tags_update**](docs/TaskTagsApi.md#task_tags_update) | **PUT** /task-tags/{id}/ | 
*TasksApi* | [**tasks_create**](docs/TasksApi.md#tasks_create) | **POST** /tasks/ | 
*TasksApi* | [**tasks_delete**](docs/TasksApi.md#tasks_delete) | **DELETE** /tasks/{id}/ | 
*TasksApi* | [**tasks_list**](docs/TasksApi.md#tasks_list) | **GET** /tasks/ | 
*TasksApi* | [**tasks_partial_update**](docs/TasksApi.md#tasks_partial_update) | **PATCH** /tasks/{id}/ | 
*TasksApi* | [**tasks_read**](docs/TasksApi.md#tasks_read) | **GET** /tasks/{id}/ | 
*TasksApi* | [**tasks_update**](docs/TasksApi.md#tasks_update) | **PUT** /tasks/{id}/ | 


## Documentation For Models

 - [AuthToken](docs/AuthToken.md)
 - [Task](docs/Task.md)
 - [TaskTag](docs/TaskTag.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

meechanic.design@gmail.com
