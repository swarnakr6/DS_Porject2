package main

import (
	"context"
	"fmt"
	"log"
	"net"
	"runtime"
	"sync"

	pb "google.golang.org/grpc/examples/helloworld/helloworld"
	"google.golang.org/grpc"
)

// function to get the  ID for each 
// of the threads runnig 
func getThreadID() string {
	buf := make([]byte, 64)
	buf = buf[:runtime.Stack(buf, false)]
	return string(buf)
}

type server struct {
	pb.PetAdoptionServiceServer
	pets  []pb.PetInfo
	mutex sync.Mutex// for our serer struct 
  //we need this to block other threads from accessing a section of the code 
  //for each thread we lcok and unlock the mutex
}

func (s *server) RegisterPet(ctx context.Context, petInfo *pb.PetInfo) (*pb.RegisterResponse, error) {
	// print out the go routine ID to show the threads 
	log.Printf("RegisterPet Thread ID: %s", getThreadID())
  // Probobly add a check to see if there is a dupe in the database
	s.mutex.Lock()
	defer s.mutex.Unlock()
  // Check if the pet is alread in the databse
	for _, pet := range s.pets {
		if pet.Name == petInfo.GetName() && pet.Breed == petInfo.GetBreed() && pet.Gender == petInfo.GetGender() {
			log.Printf("Pet %s is already in the database", petInfo.GetName())
			return &pb.RegisterResponse{Message: "Pet is already added in database"}, nil
		}
	}

	s.pets = append(s.pets, *petInfo)
	log.Printf("registered the new pet %s", petInfo.GetName())
	return &pb.RegisterResponse{Message: "Pet added to database"}, nil
}
//TODO 
//add a a way to handle images 
func (s *server) SearchPet(ctx context.Context, req *pb.SearchRequest) (*pb.SearchResponse, error) {
	// Log goroutine ID to verify concurrency
	log.Printf("SearchPet Goroutine: %s", getThreadID())

	s.mutex.Lock()
	defer s.mutex.Unlock()

	query := req.GetQuery()
	var result []*pb.PetInfo

	for _, pet := range s.pets {
		if pet.Name == query || pet.Breed == query || pet.Gender == query {
			result = append(result, &pet)
		}
	}

	if len(result) == 0 {
		return nil, fmt.Errorf("%s was not found in database", query)
	}

	return &pb.SearchResponse{Pets: result}, nil
}

func main() {
	listen, _ := net.Listen("tcp", ":50051")

	grpcServer := grpc.NewServer()
	pb.RegisterPetAdoptionServiceServer(grpcServer, &server{})

	log.Println("server running on the PORt :50051")
	grpcServer.Serve(listen)
}
