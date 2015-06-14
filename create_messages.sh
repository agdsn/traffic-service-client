#!/bin/bash

HERE=$(dirname $0)
SRC_DIR=$HERE/traffic-service-protobuf
DST_DIR=$HERE/src/traffic/messages

mkdir -p $DST_DIR
touch $DST_DIR/__init__.py

for proto in ${SRC_DIR}/*.proto ; do
    protoc -I=$SRC_DIR --python_out=$DST_DIR ${proto}
done
