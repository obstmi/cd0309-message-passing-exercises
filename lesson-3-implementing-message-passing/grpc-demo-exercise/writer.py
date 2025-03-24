import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = order_pb2.OrderMessage(
    id="1",
    created_by="Micha",
    status=order_pb2.OrderMessage.Status.PROCESSING,
    created_at="20250324",
    equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
)

response = stub.Create(order)
print("Printing the response...")
print(response)

