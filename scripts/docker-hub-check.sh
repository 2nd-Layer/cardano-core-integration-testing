#!/bin/bash

DOCKER_BASE_IMAGE=$(env DOCKER_BASE_IMAGE)
DOCKER_APPLICATION=$(env DOCKER_APPLICATION)

DOCKER_IMAGE_NAME="${DOCKER_BASE_IMAGE}-${DOCKER_APPLICATION}"
echo "Fetching image version of 2ndlayer/${DOCKER_IMAGE_NAME} from Docker Hub"

DOCKER_HUB_IMAGE_VER=$(curl -L --fail \
    "https://hub.docker.com/v2/repositories/2ndlayer/${DOCKER_IMAGE_NAME}/tags/?page_size=1000" | \
     jq '.results | .[] | .name' -r | \
     sed 's/latest//' | \
     sort --version-sort | \
    tail -n 1)