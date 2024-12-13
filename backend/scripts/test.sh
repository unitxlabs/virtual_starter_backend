#!/bin/bash

# Set variables
CONTAINER_NAME="my_test_container"
LOCAL_DIR="$(dirname "$(pwd)")"  # Use the current directory
TEST_COMMAND="pytest tests/"  # Adjust the test command as needed

# Build the Docker image using build-docker.sh
./build-docker.sh

# Run tests directly using docker run
echo "Running tests in Docker container..."
docker run --rm -v $LOCAL_DIR:/app $IMAGE_NAME $TEST_COMMAND

# Check the exit status of the test command
if [[ $? -ne 0 ]]; then
    echo "Tests failed."
    exit 1
else
    echo "Tests passed successfully!"
fi

# Clean up: stop and remove the test container
echo "Cleaning up..."
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
