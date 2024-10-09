package main

import (
	"context"
	"fmt"
	"log"
	"net"

	pb "google.golang.org/grpc/examples/helloworld/helloworld"
	"google.golang.org/grpc"
)

type server struct {
  //we need this as a place holder for the go framwork 
  //this gives a defualt for anything not impmented and makes the go compiler happy
	pb.PetAdoptionServiceServer
  // database to store our pets 
  // TODO part three make this a real database
	pets []pb.PetInfo
}

//Methdo four our server that impments pet registers from the proto. petInfo is a pointer to the 
//petifno msg defined in our proto file
func (s *server) RegisterPet(ctx context.Context, petInfo *pb.PetInfo) (*pb.RegisterResponse, error) {
	s.pets = append(s.pets, *petInfo)
	log.Printf("registered the new pet %s", petInfo.GetName())
  //returns a respones to the client with a message 
	return &pb.RegisterResponse{Message: "Pet added to datbase"}, nil
}

func (s *server) SearchPet(ctx context.Context, req *pb.SearchRequest) (*pb.SearchResponse, error) {
  //from go generate code(stub) form the proto file 
	query := req.GetQuery()
	var result []*pb.PetInfo

	for _, pet := range s.pets {
		if pet.Name == query || pet.Breed == query || pet.Gender == query {
			result = append(result, &pet)
		}
	}

	if len(result) == 0 {
		return nil, fmt.Errorf("%s was not found in the quaery ", query)
  //returns a respone back to the client
	}

  //returns a respone back to the client
	return &pb.SearchResponse{Pets: result}, nil
}

func main() {
	// Listen on port 50051
	listen, _ := net.Listen("tcp", ":50051")

	grpcServer := grpc.NewServer()
	pb.RegisterPetAdoptionServiceServer(grpcServer, &server{})

	log.Println("server started port :50051")
	grpcServer.Serve(listen)
}
