from app.Data.util.DatabaseConnector import DatabaseConnector


class DataHandler:
    _connector = DatabaseConnector()

    def get_items_from_db(self, query: str, params: tuple):
        connection = self._connector.connect()
        cursor = connection.cursor(buffered=True)
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
