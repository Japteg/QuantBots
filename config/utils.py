import json


def get_user_config(broker='zerodha'):
    with open('config/user_config.json', 'r') as user_config:
        user_config_data = json.load(user_config)
        return user_config_data.get(broker, {})
