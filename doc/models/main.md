
# Main

## Structure

`Main`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `temp` | `float` | Optional | Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. |
| `pressure` | `int` | Optional | Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa |
| `humidity` | `int` | Optional | Humidity, % |
| `temp_min` | `float` | Optional | Minimum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. |
| `temp_max` | `float` | Optional | Maximum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. |
| `sea_level` | `float` | Optional | Atmospheric pressure on the sea level, hPa |
| `grnd_level` | `float` | Optional | Atmospheric pressure on the ground level, hPa |

## Example (as JSON)

```json
{
  "temp": 293.25,
  "pressure": 1019,
  "humidity": 83,
  "temp_min": 289.82,
  "temp_max": 295.37,
  "sea_level": 984,
  "grnd_level": 990
}
```

