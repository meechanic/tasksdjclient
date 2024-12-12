# tasksdjclient.TaskTagsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_tags_create**](TaskTagsApi.md#task_tags_create) | **POST** /task-tags/ | 
[**task_tags_delete**](TaskTagsApi.md#task_tags_delete) | **DELETE** /task-tags/{id}/ | 
[**task_tags_list**](TaskTagsApi.md#task_tags_list) | **GET** /task-tags/ | 
[**task_tags_partial_update**](TaskTagsApi.md#task_tags_partial_update) | **PATCH** /task-tags/{id}/ | 
[**task_tags_read**](TaskTagsApi.md#task_tags_read) | **GET** /task-tags/{id}/ | 
[**task_tags_update**](TaskTagsApi.md#task_tags_update) | **PUT** /task-tags/{id}/ | 


# **task_tags_create**
> TaskTag task_tags_create(data)



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
api_instance = tasksdjclient.TaskTagsApi(tasksdjclient.ApiClient(configuration))
data = tasksdjclient.TaskTag() # TaskTag | 

try:
    api_response = api_instance.task_tags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTagsApi->task_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TaskTag**](TaskTag.md)|  | 

### Return type

[**TaskTag**](TaskTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_tags_delete**
> task_tags_delete(id)



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
api_instance = tasksdjclient.TaskTagsApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task tag.

try:
    api_instance.task_tags_delete(id)
except ApiException as e:
    print("Exception when calling TaskTagsApi->task_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_tags_list**
> list[TaskTag] task_tags_list(key=key, value=value, search=search, ordering=ordering)



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
api_instance = tasksdjclient.TaskTagsApi(tasksdjclient.ApiClient(configuration))
key = 'key_example' # str |  (optional)
value = 'value_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.task_tags_list(key=key, value=value, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTagsApi->task_tags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[TaskTag]**](TaskTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_tags_partial_update**
> TaskTag task_tags_partial_update(id, data)



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
api_instance = tasksdjclient.TaskTagsApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task tag.
data = tasksdjclient.TaskTag() # TaskTag | 

try:
    api_response = api_instance.task_tags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTagsApi->task_tags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task tag. | 
 **data** | [**TaskTag**](TaskTag.md)|  | 

### Return type

[**TaskTag**](TaskTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_tags_read**
> TaskTag task_tags_read(id)



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
api_instance = tasksdjclient.TaskTagsApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task tag.

try:
    api_response = api_instance.task_tags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTagsApi->task_tags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task tag. | 

### Return type

[**TaskTag**](TaskTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_tags_update**
> TaskTag task_tags_update(id, data)



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
api_instance = tasksdjclient.TaskTagsApi(tasksdjclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this task tag.
data = tasksdjclient.TaskTag() # TaskTag | 

try:
    api_response = api_instance.task_tags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTagsApi->task_tags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task tag. | 
 **data** | [**TaskTag**](TaskTag.md)|  | 

### Return type

[**TaskTag**](TaskTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

