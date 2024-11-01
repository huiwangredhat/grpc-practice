# Project Title

This is gRPC 'Hello World'

## What's gRPC]
    gRPC is a high-performance, open-source remote procedure call (RPC) framework
    developed by Google. It allows clients and servers to communicate with each
    other in a straightforward and efficient manner, regardless of the programming
    language they are implemented in.
## Installation
  ```bash
    python -m venv ~/venv-grpc
    source ~/venv-grpc/bin/activate
    pip install grpcio grpcio-tools

## How it works

    - [Define Service]: You define your service and its methods in a .proto file using Protocol Buffers.

    - [Generate Code]: Use the Protocol Buffers compiler (protoc) to generate the client and server code in your desired programming languages.
    	```bash
    	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto

    - [Implement Server]: Create a server that implements the defined service methods.

    - [Implement Client]: Create a client that calls the server's methods.

    - [Run]: Start the server and use the client to send requests and receive responses.

