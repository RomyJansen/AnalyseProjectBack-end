import mysql.connector


class DatabaseConnector:

    def connect(self, query: str):
        cnx = mysql.connector.connect(user='root',
                                      password='wachtwoord',
                                      host='localhost',
                                      database='Arnhem')

        # create a cursor object to execute queries
        cursor = cnx.cursor()

        # execute a query
        query = query
        cursor.execute(query)

        # fetch the results
        results = cursor.fetchall()

        # close the cursor and connection
        cursor.close()
        cnx.close()

        return results


if __name__ == '__main__':
    print(DatabaseConnector.connect(DatabaseConnector(), "Select * from variabelen"))
