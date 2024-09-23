from main.apps.simulation.management.commands.real_data import api

def mode(table_name_str, mode_str, api_config_path_str, api_table_path_str, backup_api_table_path_str):
    if table_name_str == "api":
        if mode_str == "create":
            api.delete_api_key_from_db()
            api.create_api_key_by_json(api_config_path_str)
        elif mode_str == "download":
            api.download_api_key_from_db(api_table_path_str)
        elif mode_str == "delete":
            api.delete_api_key_from_db()
        elif mode_str == "backup":
            api.backup_api_key_to_json(backup_api_table_path_str)
        elif mode_str == "restore":
            api.delete_api_key_from_db()
            api.restore_api_key_by_json(backup_api_table_path_str)
        else:
            print("table_name: ", table_name_str)
            print("action: not found")
