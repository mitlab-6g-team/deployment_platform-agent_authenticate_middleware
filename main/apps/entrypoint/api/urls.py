from django.urls import path
from main.utils.config import config
from main.apps.entrypoint.actors import ABMAccountManger
from main.apps.entrypoint.actors import AccountValidator
from main.apps.entrypoint.actors import Router

ENTRYPOINT_NAME=config.ENTRYPOINT.NAME

urlpatterns = [
    path(
        f'{ENTRYPOINT_NAME}/ABMAccountManger/create',
        ABMAccountManger.create
    ),
    path(
        f'{ENTRYPOINT_NAME}/AccountValidator/login',
        AccountValidator.login
    ),
    path(
        f'{ENTRYPOINT_NAME}/Router/parse/<str:api_key>',
        Router.parse
    )
]
