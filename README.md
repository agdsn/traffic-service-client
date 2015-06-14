# Traffic accounting service client

This is a example client for the [traffic-service-server](https://github.com/agdsn/traffic-service-server).

To make it work you need a working protoc compiler and python-zmq.
Yu also need to fetch the submodules. For details see the
[submodule manual](https://git-scm.com/book/de/v1/Git-Tools-Submodule).
Then run the script `create_messages.sh` to generate the protobuf
message code.

There is a script called `test_client.py` for simple testing.
Expect more to come in near future.

