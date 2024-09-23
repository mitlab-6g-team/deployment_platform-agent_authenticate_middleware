"""
This module provides a function that can help call other APIs on json request.
"""
import requests
from main.utils.config import config

def for_json(module_name_str, actor_name_str, function_name_str, payload_dict):
    """
    Sends a JSON POST request to a specified module's API endpoint.
    
    Args:
        module_name_str (str): The name of the module for which the API call is intended.
        actor_name_str (str): The name of the actor within the module.
        function_name_str (str): The specific function or endpoint within the module 
        to which the request is addressed.
        payload_dict (dict): The data to be sent with the POST request in JSON format.
    Returns:
        requests.response: The response object received from the API call.
    """

    # get the components of API path
    module_name_str = module_name_str.upper()
    module_env=getattr(config, module_name_str)

    api_root_str="api"
    module_host_ip_str=module_env.HOST_IP
    module_port_str=module_env.PORT
    module_name_str=module_env.NAME
    module_version_str=module_env.VERSION

    # get the complete API path
    host_port_str = f'http://{module_host_ip_str}:{module_port_str}/{api_root_str}/'
    route_str = f'{module_version_str}/{module_name_str}/{actor_name_str}/{function_name_str}'
    api_path_str = host_port_str + route_str

    # call API
    headers_dict={"Content-Type": "application/json"}
    response=requests.post(url=api_path_str, json=payload_dict, headers=headers_dict, timeout=30)

    return response