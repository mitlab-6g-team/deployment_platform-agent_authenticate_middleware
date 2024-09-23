from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.entrypoint.models.account import Account

@log_trigger("INFO")
@require_POST
def login(request):
    data_dict = unpacking(request)
    
    account_str = data_dict['account_name']
    password_str = data_dict['account_password']

    exist_bol = Account.objects.filter(name = account_str, password = password_str).exists()

    response_str = ""
    if exist_bol:
        response_str = "Login successfully"
        response_dict = {"detail": response_str}
        return JsonResponse(response_dict, status=200)
    else:
        response_str = "Login failed"
        response_dict = {"detail": response_str}
        return JsonResponse(response_dict, status=500)
