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

Go and docker container:

Go workSpace Setup:
start in root dir and if you have grpc-go from part2 rm it

rm -rf grpc-go

git clone -b v1.67.0 --depth 1 https://github.com/grpc/grpc-go

rm -rf grpc-go/examples

cp -r Go/part3/examples/ grpc-go/

step 1: generate .go files
cd /home/preston/Git/DS_Porject2/grpc-go/examples/helloworld/helloworld
bash compile.bash 
cd ..

step 2: build server 
cd greeter_server/
bash build.bash 

step 3: run server locally to verify it works 
./server
ctrl c // to kill the server 
cp server ../../../../Go/part3/container
cd ../../../../Go/part3/container

step 4: build and run docker 
docker build -t grpc-server .
docker run -d -p 50051:50051 --name grpc-server grpc-server


Python+docker 
