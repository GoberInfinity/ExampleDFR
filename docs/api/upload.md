# Upload

It uploads an csv file to a S3 bucket for their future retrieve

## Upload a new csv file

**Request**:

`POST` `/upload/`

Parameters:

| Name | Type | Required | Description                 |
| ---- | ---- | -------- | --------------------------- |
| file | csv  | Yes      | The csv file to be uploaded |

_Note:_

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created
```
