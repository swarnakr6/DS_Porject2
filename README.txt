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

Step-6: I created 2 files in the project directory: Python server(server.py) & Python client(client.py)

Step-7: Start the server by running command:
python server.py

Step-8:	Run the client in a separate terminal:
python client.py




Part3:
Go+docker 
Python+docker 

