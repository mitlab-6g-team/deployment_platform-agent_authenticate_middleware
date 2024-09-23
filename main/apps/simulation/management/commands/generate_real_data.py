import os
import django
from django.core.management.base import BaseCommand
from main.apps.simulation.management.commands.real_data import action

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.local')
django.setup()


class Command(BaseCommand):
    """
    This command will create a api_table.json from the api table, create an
    api table from api_config.json, back up the api table to backup_api_table.json, 
    delete all api routes from the api table, or restore api routes from backup_api_table.json 
    and create, clear role table data.
    Example: python manage.py generate_real_data --table_name=api  --action=create
    """
    help = 'Generate real data for authenticate_postgres'

    def add_arguments(self, parser):
        # 添加一個名為 `action` 的選項，用來指定要執行的函數
        parser.add_argument(
            '--table_name',
            type=str,
            help = 'Specify the table (api)'
        )

        parser.add_argument(
            '--action',
            type = str,
            help =
            '''
            Specify the action to perform (create, download, delete, 
            backup or restore for api table)'
            '''
        )

    def handle(self, *args, **options):
        table_name_str = options['table_name']
        action_str = options['action']

        api_config_path_str = 'main/apps/simulation/management/commands/real_data/json_file/api_config.json'
        api_table_path_str = 'main/apps/simulation/management/commands/real_data/json_file/api_table.json'
        backup_api_table_path_str = 'main/apps/simulation/management/commands/real_data/json_file/backup_api_table.json'

        self.stdout.write(f'Starting real {table_name_str} {action_str}')

        action.mode(
            table_name_str,
            action_str,
            api_config_path_str,
            api_table_path_str,
            backup_api_table_path_str
        )

        self.stdout.write(f'Finishing real {table_name_str} {action_str}')