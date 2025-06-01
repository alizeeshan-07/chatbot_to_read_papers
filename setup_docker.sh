#!/bin/bash

set -e

IMAGE_NAME="arxiv_papers_chatbot"

echo "Building Docker image $IMAGE_NAME ..."
docker build -t $IMAGE_NAME .

echo "Running Docker container from image $IMAGE_NAME ..."
docker run -it --env-file .env $IMAGE_NAME
