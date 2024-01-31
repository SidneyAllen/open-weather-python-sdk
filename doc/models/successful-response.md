
# Successful Response

## Structure

`SuccessfulResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coord` | [`Coord`](../../doc/models/coord.md) | Optional | - |
| `weather` | [`List[Weather]`](../../doc/models/weather.md) | Optional | (more info Weather condition codes) |
| `base` | `str` | Optional | Internal parameter |
| `main` | [`Main`](../../doc/models/main.md) | Optional | - |
| `visibility` | `int` | Optional | Visibility, meter |
| `wind` | [`Wind`](../../doc/models/wind.md) | Optional | - |
| `clouds` | [`Clouds`](../../doc/models/clouds.md) | Optional | - |
| `rain` | [`Rain`](../../doc/models/rain.md) | Optional | - |
| `snow` | [`Snow`](../../doc/models/snow.md) | Optional | - |
| `dt` | `int` | Optional | Time of data calculation, unix, UTC |
| `sys` | [`Sys`](../../doc/models/sys.md) | Optional | - |
| `id` | `int` | Optional | City ID |
| `name` | `str` | Optional | - |
| `cod` | `int` | Optional | Internal parameter |

## Example (as JSON)

```json
{
  "base": "cmc stations",
  "visibility": 16093,
  "dt": 1435658272,
  "id": 2172797,
  "name": "Cairns",
  "cod": 200,
  "coord": {
    "lon": 113.4,
    "lat": 53.5
  },
  "weather": [
    {
      "id": 28,
      "main": "main6",
      "description": "description2",
      "icon": "icon4"
    },
    {
      "id": 28,
      "main": "main6",
      "description": "description2",
      "icon": "icon4"
    }
  ],
  "main": {
    "temp": 182.98,
    "pressure": 66,
    "humidity": 110,
    "temp_min": 16.28,
    "temp_max": 48.16
  }
}
```

