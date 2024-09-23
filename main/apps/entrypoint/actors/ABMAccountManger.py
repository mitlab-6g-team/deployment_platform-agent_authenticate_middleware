from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.entrypoint.serializers.account import AccountWriteSerializer, AccountReadSerializer
from main.apps.entrypoint.services import postgres

@log_trigger("INFO")
@require_POST
def create(request):
    data_dict = unpacking(request)

    account_metadata_dict = postgres.create(AccountWriteSerializer, AccountReadSerializer, data_dict)

    response_dict = {
                        "detail": "Account created successfully",
                        "data": account_metadata_dict
                    }
    return JsonResponse(response_dict, status=200)
