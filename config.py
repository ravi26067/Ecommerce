import json

from constants import *


class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config_data = json.load(file)
        self.mysql = config_data[MYSQL]
        self.app = config_data[APP]

    def get_mysql_config(self):
        return self.mysql

    def get_app_config(self):
        return self.app

