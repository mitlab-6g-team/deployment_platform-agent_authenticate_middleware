import json
from django.utils.crypto import get_random_string
from main.utils.config import config
from main.apps.entrypoint.models.api import API
from main.apps.entrypoint.serializers.api import APIReadSerializer

def create_api_key_by_system(system_name_str, api_config_path_str):
    # 使用 with 語句打開檔案，這樣可以確保檔案在讀取後會被正確關閉
    with open(api_config_path_str, 'r') as f:
        all_api_dcit = json.load(f)

    api_version_str = ""
    if system_name_str == 'central_connector':
        api_version_str = config.CENTRAL_OPERATION.VERSION
    elif system_name_str == 'inference_connector':
        api_version_str = config.INFERENCE_OPERATION.VERSION
    elif system_name_str == 'authenticate_middleware':
        api_version_str = config.ENTRYPOINT.VERSION
    elif system_name_str == 'metadata_mgt':
        api_version_str = config.FILE_METADATA.VERSION
    
    if system_name_str == 'metadata_mgt':
        
        metadata_mgt_data = all_api_dcit.get('metadata_mgt', [])
        for module_dict in metadata_mgt_data:
            module = module_dict['module']
            api_prefix = module_dict.get('api_prefix')
            version = module_dict.get('version')
            for actor in module_dict['actor']:
                for actor_name, functionss in actor.items():
                    actor=actor_name
                    for function in functionss:
                        function=function
                        api_key_str = get_random_string(length=36)
                        API.objects.create(
                            key = api_key_str,
                            version = version,
                            system = system_name_str,
                            module = module,
                            actor = actor,
                            function = function
                        )
    else:

        system_api_dict = all_api_dcit[system_name_str]
        api_system_str = system_name_str
        api_module_str = system_api_dict["module"]

        actor_list = system_api_dict["actor"]
        for actor_dict in actor_list:
            for actor_str, function_list in actor_dict.items():
                api_actor_str = actor_str
                
                for function_str in function_list:
                    
                    api_key_str = get_random_string(length=36)
                    api_function_str = function_str
                    API.objects.create(
                        key = api_key_str,
                        version = api_version_str,
                        system = api_system_str,
                        module = api_module_str,
                        actor = api_actor_str,
                        function = api_function_str
                    )

def create_api_key_by_json(api_config_path_str):
    """
    Create api_key by api_config.json.
    
    api_config.json:
    {
        "agent_mgt": {
            "module": "agent_authentication",
            "api_prefix": "api",
            "version": "v0.1",
            "actor": [
            {
                "AuthManager": ["verify", "create", "retrieve", "upload", "delete"]
            }
            ]
        },
        .....
    }
    """
    create_api_key_by_system("central_connector", api_config_path_str)
    create_api_key_by_system("inference_connector", api_config_path_str)
    create_api_key_by_system("authenticate_middleware", api_config_path_str)
    create_api_key_by_system("metadata_mgt", api_config_path_str)

def download_api_key_from_db(api_table_path_str):
    """
    Get api_key and true_api from api table and create an api_table.json for these data.
    
    api_table.json:
    {
        "api_key":"true_api"
    }
    """
    api_model_instance = API.objects.all()
    serializer = APIReadSerializer(api_model_instance, many = True)
    api_metadata_list = serializer.data

    api_route_dict = {}

    for api_metadata_dict in api_metadata_list:
        api_key_str = api_metadata_dict['key']
        api_module_str = api_metadata_dict['module']
        api_actor_str = api_metadata_dict['actor']
        api_function_str = api_metadata_dict['function']
        service_str = f"{api_module_str}/{api_actor_str}/{api_function_str}"
        api_route_dict[api_key_str] = service_str

    with open(api_table_path_str, 'w', encoding = 'utf-8') as api_table_json:
        json.dump(api_route_dict, api_table_json, indent = 4)

def delete_api_key_from_db():
    """
    Delete all api route from api table.
    """
    API.objects.all().delete()

def backup_api_key_to_json(backup_api_table_path_str):
    """
    Download all data from api table to backup_api_table.json, except for the api_uid and api_created_time.
    
    backup_api_table.json:
    {
        "api_key":"api_dns/api_prefix/api_version/api_system/api_module/api_actor/api_function/api_description"
    }
    """
    api_model_instance = API.objects.all()
    serializer = APIReadSerializer(api_model_instance, many=True)
    api_metadata_list = serializer.data
    api_route_dict = {}

    for api_metadata_dict in api_metadata_list:
        api_prefix_str = api_metadata_dict['prefix']
        api_version_str = api_metadata_dict['version']
        api_key_str = api_metadata_dict['key']
        api_system_str = api_metadata_dict['system']
        api_module_str = api_metadata_dict['module']
        api_actor_str = api_metadata_dict['actor']
        api_function_str = api_metadata_dict['function']
        api_data_str = (f"{api_prefix_str}/{api_version_str}/{api_system_str}/"
                        f"{api_module_str}/{api_actor_str}/{api_function_str}")
        api_route_dict[api_key_str] = api_data_str

    with open(backup_api_table_path_str, 'w', encoding = 'utf-8') as backup_api_table_json:
        json.dump(api_route_dict, backup_api_table_json, indent = 4)

def restore_api_key_by_json(backup_api_table_path_str):
    """
    Create api key by backup_api_table.json.
 
    backup_api_table.json:
    {
        "api_key":"api_dns/api_prefix/api_version/api_system/api_module/api_actor/api_function/api_description"
    }
    """
    with open(backup_api_table_path_str, 'r', encoding='utf-8') as backup_api_table_json:
        api_data_dict = json.load(backup_api_table_json)

    for api_key_str, api_data_str in api_data_dict.items():
        api_data_list = api_data_str.split("/")
        api_prefix_str = api_data_list[0]
        api_version_str = api_data_list[1]
        api_system_str = api_data_list[2]
        api_module_str = api_data_list[3]
        api_actor_str = api_data_list[4]
        api_function_str = api_data_list[5]

        API.objects.create(
            key = api_key_str,
            prefix = api_prefix_str,
            version = api_version_str,
            system = api_system_str,
            module = api_module_str,
            actor = api_actor_str,
            function = api_function_str
        )
