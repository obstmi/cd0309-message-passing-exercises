# API endpoint placing an order
## HTTP Request
### Method and endpoint
POST <BASE_URL>/api/orders/
### Header
Content-Type: application/json  
(Host: localhost:8000)  
(Content-Length: 123)
### Body
```json
{  
  "brand_name": "<string>",  
  "type": "<string>",  
  "equipment": [
    "<string>"
  ],
  "customer_id": "<string>",
  "status": "<status_enum: string>"
  "created_at": "<isoformat_timestamp: string>"
}
```
## HTTP Response
### Response Code
201 Created 
### Header
Acccept: application/json  
(Host: localhost:8000)  
(Content-Length: 123)
### Body
```json
{
  "brand_name": "<string>",  
  "type": "<string>",  
  "equipment": [
    "<string>"
  ],
  "customer_id": "<string>",
  "status": "<status_enum: string>"
  "created_at": "<isoformat_timestamp: string>"
}
```

# API endpoint retrieving a list of all computer orders
## HTTP Request
### Method and endpoint
GET <BASE_URL>/api/orders/computers
### Header
Content-Type: application/json  
(Host: localhost:8000)

## HTTP Response 
### Response Code
200 OK
### Header
Accept: application/json  
(Host: localhost:8000)
### Body
```json
"computer_orders": [
  {
    "brand_name": "<string>",  
    "type": "<string>",  
    "equipment": [
      "<string>"
    ],
    "customer_id": "<string>",
    "status": "<status_enum: string>"
    "created_at": "<isoformat_timestamp: string>"
  }
]
```
