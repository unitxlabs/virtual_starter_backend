#!/bin/bash

# Set variables
IMAGE_NAME="my-production-image"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
cd "${PARENT_DIR}" || exit 1

# Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Check if the build was successful
if [[ $? -ne 0 ]]; then
    echo "Error: Docker image build failed."
    exit 1
else
    echo "Docker image $IMAGE_NAME built successfully!"
fi
