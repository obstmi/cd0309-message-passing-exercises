```JavaScript

syntax = "proto3";

// message for an order
message OrderMessage {  
  string brand_name = 1;
  string type = 2;
  repeated string equipment = 3;
  string customer_id = 4;
  string status = 5;
  string created_at = 6;
  string order_id = 7;
}

// enhanced message for an order
message OrderMessage_1 {  
    enum Status {
    QUEUED = 0;
    PROCESSING = 1;
    COMPLETED = 2;
    FAILED = 3;
  }

    enum Equipment {
    Keyboard = 0;
    Mouse = 1;
    Webcam = 2;
    Monitor = 3;
  }

  string brand_name = 1;
  string type = 2;
  repeated Equipment equipment = 3;
  string customer_id = 4;
  Status status = 5 [ default = QUEUED ];
  string created_at = 6;
  string order_id = 7;
}

// service definition for an order
service OrderService {
  rpc Create(OrderMessage) returns (OrderMessage)
}

// message for a list of orders
message OrderList {
  repeated Order order_list = 1;
}

// service definition for a list of orders
service OrderListService {
  rpc GetOrders(OrderListRequest) returns (OrderList)
}

```
