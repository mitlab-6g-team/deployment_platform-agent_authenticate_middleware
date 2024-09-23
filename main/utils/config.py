import os
from dotenv import load_dotenv
from dataclasses import dataclass

# Initialization
load_dotenv(".env.common")
load_dotenv('.env', override=True)

@dataclass
class ServerConfig:
    """
       Server config
    """
    HOST_IP: str
    PORT: str
    NAME: str
    VERSION: str

@dataclass
class PostgreConfig:
    """
       Postgres config
    """
    ENGINE: str
    NAME: str
    HOST_IP: str
    PORT: str
    USER: str
    PASSWORD: str

@dataclass
class Config:
    """
        Config sets
    """
    LOGS_FOLDER_PATH: str
    DJANGO_SETTINGS_MODULE: str
    DEBUG: str
    ALLOWED_HOSTS: str

    POSTGRES:PostgreConfig
    AGENT_OPERATION:ServerConfig
    CENTRAL_OPERATION:ServerConfig
    INFERENCE_OPERATION:ServerConfig
    ENTRYPOINT:ServerConfig
    ABSTRACT_METADATA:ServerConfig
    FILE_METADATA:ServerConfig

config = Config(
    #Default 
    LOGS_FOLDER_PATH=os.getenv("LOGS_FOLDER_PATH"),
    DJANGO_SETTINGS_MODULE=os.getenv("DJANGO_SETTINGS_MODULE"),
    DEBUG=os.getenv("DEBUG"),
    ALLOWED_HOSTS=os.getenv("ALLOWED_HOSTS"),

    #POSTGRES
    POSTGRES=PostgreConfig(
        ENGINE=os.getenv("HTTP_POSTGRES_DATABASE_ENGINE"),
        NAME=os.getenv("HTTP_POSTGRES_DATABASE_NAME"),
        HOST_IP=os.getenv("HTTP_POSTGRES_HOST_IP"),
        PORT=os.getenv("HTTP_POSTGRES_PORT"),
        USER=os.getenv("HTTP_POSTGRES_USER"),
        PASSWORD=os.getenv("HTTP_POSTGRES_PASSWORD"),
    ),
    # abstract_metadata
    ABSTRACT_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_ABSTRACT_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_ABSTRACT_METADATA_PORT"),
        NAME=os.getenv("HTTP_ABSTRACT_METADATA_NAME"),
        VERSION=os.getenv("HTTP_ABSTRACT_METADATA_VERSION"),
    ),
    # file_metadata
    FILE_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_METADATA_PORT"),
        NAME=os.getenv("HTTP_FILE_METADATA_NAME"),
        VERSION=os.getenv("HTTP_FILE_METADATA_VERSION"),
    ),
    # central-layer.agent_mgt.agent_connector.agent_operation
    AGENT_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_AGENT_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_AGENT_OPERATION_PORT"),
        NAME=os.getenv("HTTP_AGENT_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_AGENT_OPERATION_VERSION"),
    ),
    #agent-layer.agent_mgt.central_connector.central_operation
    CENTRAL_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_CENTRAL_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_CENTRAL_OPERATION_PORT"),
        NAME=os.getenv("HTTP_CENTRAL_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_CENTRAL_OPERATION_VERSION"),
    ),
    #agent-layer.agent_mgt.inference_connector.inference_operation
    INFERENCE_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_INFERENCE_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_INFERENCE_OPERATION_PORT"),
        NAME=os.getenv("HTTP_INFERENCE_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_INFERENCE_OPERATION_VERSION"),
    ),
    #agent-layer.agent_mgt.authenticate_middleware.entrypoint
    ENTRYPOINT=ServerConfig(
        HOST_IP=os.getenv("HTTP_ENTRYPOINT_HOST_IP"),
        PORT=os.getenv("HTTP_ENTRYPOINT_PORT"),
        NAME=os.getenv("HTTP_ENTRYPOINT_NAME"),
        VERSION=os.getenv("HTTP_ENTRYPOINT_VERSION"),
    )
)
