Part1:

Part2:

Go: 
-Preston Mann
I used the hellowrold as a starting point from the go GRPC tutorial
I removed the helloworld files and replaced it with the GO server and client 
for the project 

Go WorkSpace setup:

git clone -b v1.67.0 --depth 1 https://github.com/grpc/grpc-go
rm -rf grpc-go/examples
cp -r Go/part2/examples grpc-go/



Step 1: Generate .go files
cd grpc-go/examples/helloworld/helloworld
bash compile.bash 
cd ..

Step 2: run server
cd greeter_server
bash run.bash 

Step 3: run client 
open a new terminal tab
cd /grpc-go/examples/helloworld/greeter_client
bash run.bash 

Python:


Part3:
Go+docker 
Python+docker 
