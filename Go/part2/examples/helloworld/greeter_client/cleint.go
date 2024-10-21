package main

import (
	"context"
	"log"
	"os"
	"time"

	pb "google.golang.org/grpc/examples/helloworld/helloworld"
	"google.golang.org/grpc"
)
func add() {
  conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	client := pb.NewPetAdoptionServiceClient(conn)

	pet := &pb.PetInfo{
		Name:   "Test",
		Breed:  "NA",
		Gender: "Male",
		Age:    -1,
	}

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	res, err := client.RegisterPet(ctx, pet)
	if err != nil {
		log.Fatalf("could not register pet: %v", err)
	}
	log.Printf("Pet Registration Response: %s", res.GetMessage())


}

func search(){
  conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()


	client := pb.NewPetAdoptionServiceClient(conn)


	query := "Test"
	if len(os.Args) > 1 {
		query = os.Args[1]
	}

	searchReq := &pb.SearchRequest{Query: query}
	searchRes, err := client.SearchPet(ctx, searchReq)
	if err != nil {
		log.Fatalf("could not search for pets: %v", err)
	}

	log.Println("Pets found:")
	for _, pet := range searchRes.GetPets() {
		log.Printf("Name: %s, Breed: %s, Gender: %s, Age: %d", pet.GetName(), pet.GetBreed(), pet.GetGender(), pet.GetAge())
	}

}

func main() {
  add();
  search();
}
