from concurrent import futures
import grpc
import pet_adoption_pb2
import pet_adoption_pb2_grpc

# In-memory database to store pets
pets_db = []


class PetAdoptionService(pet_adoption_pb2_grpc.PetAdoptionServiceServicer):
    def RegisterPet(self, request, context):
        pets_db.append(request)
        return pet_adoption_pb2.RegisterResponse(
            message=f"Pet {request.name} registered successfully."
        )

    def SearchPet(self, request, context):
        results = [
            pet
            for pet in pets_db
            if request.query.lower()
            in (pet.name.lower(), pet.breed.lower(), pet.gender.lower())
        ]
        return pet_adoption_pb2.SearchResponse(pets=results)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pet_adoption_pb2_grpc.add_PetAdoptionServiceServicer_to_server(
        PetAdoptionService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

