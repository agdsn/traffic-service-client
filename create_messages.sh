#!/bin/bash

HERE=$(dirname $0)
SRC_DIR=$HERE/traffic-service-protobuf
DST_DIR=$HERE/src/traffic/messages

mkdir -p $DST_DIR

for proto in replies requests; do
    protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/${proto}.proto
done
