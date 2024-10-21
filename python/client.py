import grpc
from google.protobuf.empty_pb2 import Empty
from message_pb2 import Pet, SearchRequest
from message_pb2_grpc import PetAdoptionServiceStub

def register_pet(stub, name, gender, age, breed, picture_url):
    pet = Pet(name=name, gender=gender, age=age, breed=breed, picture_url=picture_url)
    response = stub.RegisterPet(pet)
    print(response.message)

def search_pet(stub, query):
    search_request = SearchRequest(query=query)
    response = stub.SearchPet(search_request)
    print(f"Found {len(response.pets)} pets matching '{query}':")
    for pet in response.pets:
        print(f"Name: {pet.name}, Gender: {pet.gender}, Age: {pet.age}, Breed: {pet.breed}, Picture: {pet.picture_url}")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = PetAdoptionServiceStub(channel)
        # Example of registering a pet
        register_pet(stub, "Buddy", "Male", 3, "Golden Retriever", "http://example.com/buddy.jpg")
        # Example of searching for a pet
        search_pet(stub, "Buddy")

if __name__ == "__main__":
    run()
