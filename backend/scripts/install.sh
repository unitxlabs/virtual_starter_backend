#!/bin/bash

# Set variables
TAR_FILE="my_image.tar"
IMAGE_NAME="my-production-image"

# Check if the tar file exists
if [[ ! -f $TAR_FILE ]]; then
    echo "Error: $TAR_FILE does not exist."
    exit 1
fi

# Load the Docker image
echo "Importing Docker image from $TAR_FILE..."
docker load -i $TAR_FILE

echo "Docker image $IMAGE_NAME imported successfully!"
