# tasksdjclient.TasksApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_create**](TasksApi.md#tasks_create) | **POST** /tasks/ | 
[**tasks_delete**](TasksApi.md#tasks_delete) | **DELETE** /tasks/{id}/ | 
[**tasks_list**](TasksApi.md#tasks_list) | **GET** /tasks/ | 
[**tasks_partial_update**](TasksApi.md#tasks_partial_update) | **PATCH** /tasks/{id}/ | 
[**tasks_read**](TasksApi.md#tasks_read) | **GET** /tasks/{id}/ | 
[**tasks_update**](TasksApi.md#tasks_update) | **PUT** /tasks/{id}/ | 


# **tasks_create**
> Task tasks_create(data)



API endpoint that represents a list of objects.

### Example
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
api_instance = tasksdjclient.TasksApi(tasksdjclient.ApiClient(configuration))
data = tasksdjclient.Task() # Task | 

try:
    api_response = api_instance.tasks_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_delete**
> tasks_delete(id)



API endpoint that represents a list of objects.

### Example
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
api_instance = tasksdjclient.TasksApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task.

try:
    api_instance.tasks_delete(id)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_list**
> list[Task] tasks_list(name=name, human_description=human_description, search=search, ordering=ordering)



API endpoint that represents a list of objects.

### Example
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
api_instance = tasksdjclient.TasksApi(tasksdjclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
human_description = 'human_description_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.tasks_list(name=name, human_description=human_description, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **human_description** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_partial_update**
> Task tasks_partial_update(id, data)



API endpoint that represents a list of objects.

### Example
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
api_instance = tasksdjclient.TasksApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task.
data = tasksdjclient.Task() # Task | 

try:
    api_response = api_instance.tasks_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task. | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_read**
> Task tasks_read(id)



API endpoint that represents a list of objects.

### Example
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
api_instance = tasksdjclient.TasksApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task.

try:
    api_response = api_instance.tasks_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task. | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update**
> Task tasks_update(id, data)



API endpoint that represents a list of objects.

### Example
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
api_instance = tasksdjclient.TasksApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task.
data = tasksdjclient.Task() # Task | 

try:
    api_response = api_instance.tasks_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task. | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

