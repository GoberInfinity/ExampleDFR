# Upload

It uploads an csv file to a S3 bucket for their future retrieve. The structure of the csv file should be the following one:

| transaction_id                       | transaction_date | transaction_amount | client_id | client_name |
| ------------------------------------ | ---------------- | ------------------ | --------- | ----------- |
| 87916ec9-2142-4287-9601-c6c871e2bab9 | 2016-10-01       | 769                | 728       | Dawn Roll   |

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
