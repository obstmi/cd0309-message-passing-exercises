import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a getter that can be used to get messages to gRPC.
"""

print("Getting sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Define empty payload
empty = order_pb2.Empty()

response = stub.Get(empty)
print(response)

