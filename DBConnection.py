import sqlite3
import re

class DBConnection:
    def __init__(self, table_name, column_names, column_types, data_insert, db_name):
        self.db_name = db_name
        self.table_name = table_name
        self.column_names = column_names
        self.column_types = column_types
        self.data_insert = data_insert
        # Create the database and establish connection using context manager
        with sqlite3.connect(self.db_name) as conn:
            self.conn = conn
            self.cursor = conn.cursor()
    # Method create_table that creates a table with the given name, column names, and column types if it does not exist.
    def create_table(self):
        columns = ", ".join([f"{name} {dtype}" for name, dtype in zip(self.column_names, self.column_types)])
        create_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columns})"
        self.cursor.execute(create_query)
        self.conn.commit()
    # Method insert_data that inserts a given row into the given table if it does not already exist.
    def insert_data(self):
        self.cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns_info = self.cursor.fetchall()
        column_names = [col[1] for col in columns_info]  # corrected index to get column name
        datetime_pattern = r"\d{2}/\d{2}/\d{4} \d{2}\.\d{2}" # pattern to exclude current date time value column from duplicates check
        # Build where_clause, excluding columns where the corresponding value matches the datetime pattern
        where_parts = []
        values_for_where = []
        for col, val in zip(column_names, self.data_insert):
            if not re.match(datetime_pattern, str(val)):
                where_parts.append(f"lower({col}) = lower(?)") # case-insensitive
                values_for_where.append(val)
        where_clause = " AND ".join(where_parts) # where clause for duplicates check, case-insensitive, not include column with current date time
        select_query = f"SELECT 1 FROM {self.table_name} WHERE {where_clause} LIMIT 1"
        self.cursor.execute(select_query, values_for_where)
        exists = self.cursor.fetchone()
        if exists:
            #print(f"Сase-insensitive data row: {self.data_insert} already exists in {self.table_name} table of {self.db_name}. No insertion performed.\n")
            pass
        else:
            join_data_insert = ", ".join(["?"] * len(self.data_insert))
            insert_query = f"INSERT INTO {self.table_name} VALUES ({join_data_insert})"
            self.cursor.execute(insert_query, self.data_insert)
            self.conn.commit()
            #print(f"Row {self.data_insert} inserted into {self.table_name} table of {self.db_name} successfully.\n")

    # Method that retrieves a row for a specific column value
    def select_data (self, column_value):
        self.cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns_info = self.cursor.fetchall()
        column_names = [col[1] for col in columns_info]
        column_names_str = ", ".join(column_names)
        where_clause = f"LOWER({column_names[0]}) = LOWER(?)"
        self.cursor.execute(f"SELECT {column_names_str} FROM {self.table_name} WHERE {where_clause}",(column_value,))
        result = self.cursor.fetchone()
        return result



