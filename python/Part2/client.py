import grpc
import pet_adoption_pb2
import pet_adoption_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pet_adoption_pb2_grpc.PetAdoptionServiceStub(channel)

        # Register a new pet
        pet_info = pet_adoption_pb2.PetInfo(
            name="Buddy", breed="Golden Retriever", gender="Male", age=3
        )
        response = stub.RegisterPet(pet_info)
        print(f"Register Response: {response.message}")

        # Search for a pet by name
        search_request = pet_adoption_pb2.SearchRequest(query="Buddy")
        search_response = stub.SearchPet(search_request)
        for pet in search_response.pets:
            print(
                f"Found Pet: {pet.name}, {pet.breed}, {pet.gender}, {pet.age} years old"
            )


if __name__ == "__main__":
    run()
