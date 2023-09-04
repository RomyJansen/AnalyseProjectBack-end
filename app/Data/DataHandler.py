import mysql.connector

from app.Data.util.DatabaseConnector import DatabaseConnector


class DataHandler:
    _connector = DatabaseConnector()

    def get_items_from_db(self, query: str, params: tuple):
        connection = self._connector.connect()
        try:
            cursor = connection.cursor(buffered=True)
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as e:
            print("An error occurred: ", e)
            raise

        finally:
            connection.close()
        return results

    def add_item_to_db(self, query: str, params: tuple):
        connection = self._connector.connect()
        try:
            cursor = connection.cursor(buffered=True)
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print("An error occurred: ", e)
            raise
        finally:
            connection.close()
