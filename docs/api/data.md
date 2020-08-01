# Data

It retrieves all the data after being uploaded into the S3 bucket, it supports order by column and search

## Retrieve data from csv

**Request**:

`GET` `/data/`

_Note:_

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

{
  "transaction_id": "87916ec9-2142-4287-9601-c6c871e2bab9",
  "transaction_date": "2016-10-01",
  "transaction_amount": "769",
  "client_id": "728",
  "client_name": "Dawn Rolls",
}
'''
```
