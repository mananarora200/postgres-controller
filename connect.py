import psycopg2
import time
import main
connection = psycopg2.connect(user = "postgres",
                                password = "qwertyuiop",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "jarvis")
cursor = connection.cursor()    

def connect_db():
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
    time.sleep(2)
    main.menu()
def close_db():
    if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    time.sleep(2)
    main.menu()
def create_table():
    table_name = input("Enter table name: ")
    query = ''
    for i in range(int(input("Enter no. of columns: "))):
        col_name = input(f"enter name of your {i+1} column: ")
        query += f" {col_name}"
        if 'PRIMARY KEY' not in query:
                ask = input("want to add primary key (y/n): ")
                if ask == 'y':
                    data_type = input("1. serial\n2. integer\n3. varchar\n4. char\n5. TEXT\nSelect datatype :")
                    if data_type == '1':
                        query += " serial"
                    elif data_type == '2':
                        query += " integer"
                    elif data_type == '3':
                        query += " varchar"
                    elif data_type == '4':
                        query += " char"
                    elif data_type == '5':
                        query += " TEXT"
                    else:
                        query += " varchar"
                    query += " PRIMARY KEY,"
                else:
                    data_type = input("1. serial\n2. integer\n3. varchar\n4. char\n5. TEXT\nSelect datatype :")
                    if data_type == '1':
                        query += " serial,"
                    elif data_type == '2':
                        query += " integer,"
                    elif data_type == '3':
                        query += " varchar,"
                    elif data_type == '4':
                        query += " char,"
                    elif data_type == '5':
                        query += " TEXT,"
                    else:
                        query += " varchar,"
        else:
            data_type = input("1. serial\n2. integer\n3. varchar\n4. char\n5. TEXT\nSelect datatype :")
            if data_type == '1':
                query += " serial,"
            elif data_type == '2':
                query += " integer,"
            elif data_type == '3':
                query += " varchar,"
            elif data_type == '4':
                query += " char,"
            elif data_type == '5':
                query += " TEXT,"
            else:
                query += " varchar,"
    cursor.execute(f"CREATE TABLE {table_name} ({query[1:-1]});")
    connection.commit()
    main.menu()
def show_tables():
    cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    tables = cursor.fetchall()
    tables_str = ""
    for i,k in enumerate(tables):
        for j in k:
            tables_str += f"\n{i+1} {j}"
    print(tables_str)
    input("press enter")
    main.menu()
def delete_table():
    list_table = []
    cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    tables = cursor.fetchall()
    tables_str = ""
    for i,k in enumerate(tables):
        for j in k:
            list_table.append(j)
            tables_str += f"\n{i+1} {j}"
    print(tables_str)
    check = int(input("Select Table"))
    cursor.execute(f"DROP TABLE {list_table[check-1]}")
    connection.commit()
    main.menu()
def get_rows():
    list_table = []
    cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    tables = cursor.fetchall()
    tables_str = ""
    for i,k in enumerate(tables):
        for j in k:
            list_table.append(j)
            tables_str += f"\n{i+1} {j}"
    print(tables_str)
    check = int(input("Select Table"))
    cursor.execute(f"select * from {list_table[check-1]}")
    columns_fetch = cursor.fetchall()
    print(columns_fetch)
    input("Enter to continue")
    main.menu()
def insert_row():
    list_table = []
    cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    tables = cursor.fetchall()
    tables_str = ""
    for i,k in enumerate(tables):
        for j in k:
            list_table.append(j)
            tables_str += f"\n{i+1} {j}"
    print(tables_str)
    check = int(input("Select Table: "))
    cursor.execute(f"Select * FROM {list_table[check-1]} LIMIT 0")
    colnames = [desc[0] for desc in cursor.description]
    col_str = ""
    value_str = ""
    record = []
    for i in colnames:
        val_col = input(f"enter value for {i}: ")
        col_str += f" {i},"
        value_str += " %s,"
        record.append(val_col)
    postgres_insert_query = f""" INSERT INTO {list_table[check-1]} ({col_str[1:-1]}) VALUES ({value_str[1:-1]})"""
    record_to_insert = tuple(record)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    main.menu()
def delete_row():
    list_table = []
    cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    tables = cursor.fetchall()
    tables_str = ""
    for i,k in enumerate(tables):
        for j in k:
            list_table.append(j)
            tables_str += f"\n{i+1} {j}"
    print(tables_str)
    check = int(input("Select Table: "))
    sql_delete_query = f"""Delete from {list_table[check-1]}"""
    cursor.execute(sql_delete_query)
    connection.commit()
    main.menu()
def update_row():
    #sql_update_query = """Update mobile set price = %s where id = %s"""
    main.menu()