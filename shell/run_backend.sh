#!/bin/bash
# entrypoint: mitlab-6g-agent-dashboard

source .env.common
source .env

docker build \
    --tag ${BACKEND_IMAGE_NAME} \
    .

docker rm -f ${BACKEND_CONTAINER_NAME}
docker run \
    --restart=always \
    --name ${BACKEND_CONTAINER_NAME} \
    -p ${BACKEND_CONTAINER_PORT}:8000 \
    -v ${BACKEND_PATH}:/app/agent_authenticate_middleware \
    --env-file=${BACKEND_ENV_PATH} \
    -itd ${BACKEND_IMAGE_NAME}:latest \
    bash ./shell/backend_init.sh