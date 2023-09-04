import configparser

import mysql.connector


class DatabaseConnector:

    def connect(self, ):
        config = configparser.ConfigParser()

        config.read('config.ini')
        cnx = mysql.connector.connect(user=config.get('DatabaseSection', 'database.user'),
                                      password=config.get('DatabaseSection', 'database.password'),
                                      host=config.get('DatabaseSection', 'database.host'),
                                      database=config.get('DatabaseSection', 'database.dbname'))

        return cnx
