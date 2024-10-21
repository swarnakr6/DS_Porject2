import grpc
import pet_adoption_pb2
import pet_adoption_pb2_grpc
from PIL import Image
import io
import os


def register_pet(stub, pet_info):
    response = stub.RegisterPet(pet_info)
    print(f"Register Response: {response.message}")


def display_image(image_data, pet_name):
    image = Image.open(io.BytesIO(image_data))
    image.show()

    current_directory = os.getcwd()
    image_save_path = os.path.join(
        current_directory, f"From_Server_{pet_name}.png"
    )  # Save as PNG
    image.save(image_save_path)
    print(f"Image saved to {image_save_path}")


def search_pet(stub):
    query = input("Enter name, breed, or gender to search for a pet: ")
    # the server will return multiple entries
    search_request = pet_adoption_pb2.SearchRequest(query=query)
    try:
        search_response = stub.SearchPet(search_request)
        if search_response.pets:
            for pet in search_response.pets:
                print(
                    f"pet found! : {pet.name}, {pet.breed}, {pet.gender}, {pet.age} years old"
                )
                if pet.image:
                    print(f"Displaying image for {pet.name}...")
                    display_image(pet.image, pet.name)
                else:
                    print("No image available for the pet")
        else:
            print("No pets found for the search.")

    except grpc.RpcError as e:
        print(f"Error occurred while searching for pet: {e.details()}")


def read_pets_from_file(file_path):
    # util code to parse file
    pets = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) == 5:
                    name, breed, gender, age, image = fields
                    pets.append(
                        {
                            "name": name.strip(),
                            "breed": breed.strip(),
                            "gender": gender.strip(),
                            "age": int(age.strip()),
                            "image": image.strip(),
                        }
                    )
    except Exception as e:
        print(f"Error while reading file: {e}")
    return pets


def read_image(file_path):
    try:
        with open(file_path, "rb") as image_file:
            return image_file.read()
    except Exception as e:
        print(f"Error reading image file {file_path}: {e}")
        return b""  # empty retrun if not found


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pet_adoption_pb2_grpc.PetAdoptionServiceStub(channel)
        while True:
            print("\nChoose an option:")
            print("1. Register pets from file: ")
            print("2. Search for a pet: ")
            print("3. Exit: ")
            choice = input("Enter a choice: ")

            if choice == "1":
                file_path = input(
                    "Enter the path to the text file containing the pets: "
                )
                pets_data = read_pets_from_file(file_path)

                for pet in pets_data:
                    image_bytes = read_image(pet.get("image", ""))
                    pet_info = pet_adoption_pb2.PetInfo(
                        name=pet["name"],
                        breed=pet["breed"],
                        gender=pet["gender"],
                        age=pet["age"],
                        image=image_bytes,
                    )
                    register_pet(stub, pet_info)

            elif choice == "2":
                search_pet(stub)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choich try again")


if __name__ == "__main__":
    run()
