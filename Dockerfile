FROM python:3.8.10

WORKDIR /app/agent_authenticate_middleware

COPY . .

RUN apt-get update \
    && apt-get install -y libpq-dev \
    && pip install -r /app/agent_authenticate_middleware/requirements/local.txt