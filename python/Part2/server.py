import grpc
from concurrent import futures
import time
import message_pb2
import message_pb2_grpc
from google.protobuf import empty_pb2  # Import the empty message

class PetAdoptionService(message_pb2_grpc.PetAdoptionServiceServicer):
    def GetMessage(self, request, context):
        # Respond with a simple message
        return message_pb2.MessageResponse(message="Welcome to the Virtual Pet Adoption System!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_PetAdoptionServiceServicer_to_server(PetAdoptionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on 50051...")
    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
