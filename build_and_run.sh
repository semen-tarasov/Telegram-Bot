#!/bin/bash -xe

docker build -t bot .
docker run -i -d -t bot
