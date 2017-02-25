import sqlite3
# ref http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html

class StockSQLiteDB:
    def __init__(self, db_name='stocklab.sqlite'):
        self.db_name = db_name

    def get_sqlite_version(self):
        with sqlite3.connect(self.db_name) as connection:
            return connection.cursor().execute('SELECT SQLITE_VERSION()').fetchone()

    def get_datalist(self, table_name, filters = '1=1'):
        with sqlite3.connect(self.db_name) as connection:
            statement = "SELECT * FROM " + table_name + " WHERE " + filters
            return connection.cursor().execute(statement).fetchall()

    def get_data_scal_item(self, table_name, filters):
        if filters:
            with sqlite3.connect(self.db_name) as connection:
                statement = "SELECT * FROM " + table_name + " WHERE " + filters
                return connection.cursor().execute(statement).fetchone()

    def insert_to_table(self, table_name, data_tuple_list):
        if data_tuple_list[0]:
            statement_ref = ','.join(['?' for dataitem in data_tuple_list[0]])
            with sqlite3.connect(self.db_name) as connection:
                try:
                    connection.cursor().executemany("INSERT INTO " + table_name + " VALUES (" + statement_ref +")", data_tuple_list)
                    connection.commit()
                except sqlite3.Error as e:
                    if connection:
                        connection.rollback()

    def delete_from_table(self, table_name, filters = '1=1'):
        with sqlite3.connect(self.db_name) as connection:
            try:
                if filters:
                    connection.cursor().execute("DELETE FROM " + table_name + " WHERE " + filters)
                else:
                    connection.cursor().execute("DELETE FROM " + table_name)
                connection.commit()
            except sqlite3.Error as e:
                if connection:
                    connection.rollback()