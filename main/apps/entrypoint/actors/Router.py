from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.entrypoint.models.api import API
from main.apps.entrypoint.serializers.api import APIReadSerializer
from main.apps.entrypoint.services import postgres
from main.utils.config import config
from main.utils import request

@log_trigger("INFO")
@require_POST
def parse(router_request, api_key):

    metadata_dict = postgres.retrieve(
                        API,
                        APIReadSerializer,
                        api_key
    )

    api_module_str = metadata_dict["module"]
    api_actor_str = metadata_dict["actor"]
    api_function_str = metadata_dict["function"]

    payload_dict = unpacking(router_request)
    response = request.for_json(api_module_str, api_actor_str, api_function_str, payload_dict)

    response_dict = response.json()
    status_code_int = response.status_code
    return JsonResponse(response_dict, status=status_code_int)
