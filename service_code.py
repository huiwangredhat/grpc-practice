import grpc
from concurrent import futures
import time
import service_pb2
import service_pb2_grpc

class Greeter(service_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return service_pb2.HelloResponse(message='Hello, ' + request.name)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("Server is running on port 50051...")
server.wait_for_termination()

