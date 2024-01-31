
# Weather

## Structure

`Weather`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Weather condition id |
| `main` | `str` | Optional | Group of weather parameters (Rain, Snow, Extreme etc.) |
| `description` | `str` | Optional | Weather condition within the group |
| `icon` | `str` | Optional | Weather icon id |

## Example (as JSON)

```json
{
  "id": 803,
  "main": "Clouds",
  "description": "broken clouds",
  "icon": "50d"
}
```

