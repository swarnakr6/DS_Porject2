FROM python:3.9
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN pip install grpcio grpcio-tools
RUN pip install protobuf==5.27.2
CMD ["python", "client.py"]
