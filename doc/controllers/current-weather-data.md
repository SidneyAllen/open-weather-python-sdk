# Current Weather Data

```python
current_weather_data_controller = client.current_weather_data
```

## Class Name

`CurrentWeatherDataController`


# Current Weather Data

Get the current weather info

```python
def current_weather_data(self,
                        q=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `q` | `str` | Query, Optional | For the query value, type the city name and optionally the country code divided by comma; use ISO 3166 country codes. |

## Response Type

[`SuccessfulResponse`](../../doc/models/successful-response.md)

## Example Usage

```python
result = current_weather_data_controller.current_weather_data()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found response | `APIException` |

