Part1:

Part2:

Go: 
-Preston Mann
I used the hellowrold as a starting point from the go GRPC tutorial
I removed the helloworld files and replaced it with the GO server and client 
for the project 

Step 1:
bash grpc-go/examples/helloworld/helloworld/compile.bash

Step 2: run server
bash grpc-go/examples/helloworld/greeter_server/run.bash

Step 3: run client 
bash grpc-go/examples/helloworld/greeter_client/run.bash


Python:
-Swarna Kannambadi Ramesh

Step-1: Python Workspace setup:
I Installed gRPC & gRPC tools by running the following 2 commands:
python -m pip install grpcio 
python -m pip install grpcio-tools

Step-2: I Cloned the repository:
git clone -b v1.66.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc

Step-3: Navigate to the project directory.

Step-4: I created a proto(pet_adoption.proto) file in the project directory.

Step-5: From the project directory, ran the following command to generate the necessary Python files from the proto file(pet_adoption_pb2.py & pet_adoption_pb2_grpc.py):
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pet_adoption.proto

Step-6: I created 2 files(code) in the project directory: Python server(server.py) & Python client(client.py)

Step-7: Start the server by running command:
python server.py

Step-8:	Run the client in a separate terminal:
python client.py




Part3:
Go+docker 
Python+docker:
-Swarna Kannambadi Ramesh

Step-1:  I used the same proto file with the required updates(included the image details)

Step-2: I retained the server file from Part2 & implemented Python client by making changes to the client file(code)

Step-3: I containerized the Python client Using Docker: 
created a separate Dockerfile in the directory where my Python client code was located.

Step-4: Build the Docker container using the following command:
docker build -t pet-adoption-server 

Step-5: Run the Docker container using the following command:
docker run -p 50051:50051 pet-adoption-server


