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

I created 3 files: a proto(pet_adoption.proto) file, Python server(server.py) & Python client(client.py) in the project directory.

Step-1: From the project directory, ran the following command to generate the necessary Python files from the proto file(pet_adoption_pb2.py & pet_adoption_pb2_grpc.py):
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pet_adoption.proto

Step-2: Start the server by running command:
python server.py

Step-3:6)	Run the client in a separate terminal:
python client.py




Part3:
Go+docker 
Python+docker 

