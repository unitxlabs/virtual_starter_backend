#!/bin/bash

# Set variables
IMAGE_NAME="my-production-image"
TAR_FILE="my_image.tar"
PACKAGE_FILE="package.zip"
INSTALL_SCRIPT="install.sh"
START_SCRIPT="start.sh"

# Build Docker image
./build-docker.sh

# Export Docker image to tar file
echo "Exporting Docker image to $TAR_FILE..."
docker save -o $TAR_FILE $IMAGE_NAME

# Check if install and start scripts exist
if [[ ! -f $INSTALL_SCRIPT ]]; then
    echo "Error: $INSTALL_SCRIPT does not exist."
    exit 1
fi

if [[ ! -f $START_SCRIPT ]]; then
    echo "Error: $START_SCRIPT does not exist."
    exit 1
fi

# Create a package and compress the files
echo "Creating package $PACKAGE_FILE..."
zip $PACKAGE_FILE $INSTALL_SCRIPT $START_SCRIPT $TAR_FILE

# docker push $IMAGE_NAME
# Clean up temporary files
echo "Cleaning up..."
rm $TAR_FILE

echo "Package $PACKAGE_FILE created successfully!"
