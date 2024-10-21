FROM python:3.9
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN apt-get update && apt-get install -y \
    imagemagick \
    python3-pip \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install grpcio grpcio-tools
RUN pip install protobuf==5.27.2
RUN pip install pillow
EXPOSE 50051
CMD ["python", "client.py"]
