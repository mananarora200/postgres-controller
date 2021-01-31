import os
import time
import connect
import sys
menu_str = """
1. Connect to a Database
2. Close Connection
3. Create a new table
4. Delete a table
5. Get rows from a table
6. Insert a row in a table
7. Delete a row in a table
8. Update a row in a table
9. Show all tables
10. Exit
"""
def menu():
    os.system("cls")
    print(menu_str)
    a = input("Enter your choice: ")
    if a=="1":
        connect.connect_db()
    elif a=="2":
        connect.close_db()
    elif a=="3":
        connect.create_table()
    elif a=="4":
        connect.delete_table()
    elif a=="5":
        connect.get_rows()
    elif a=="6":
        connect.insert_row()
    elif a=="7":
        connect.delete_row()
    elif a=="8":
        connect.update_row()
    elif a=="9":
        connect.show_tables()
    elif a=="10":
        print("Thank you for using Postgres controller !!")
        time.sleep(1)
        sys.exit()
    else:
        print("Enter vaild choice")
        time.sleep(1)
        menu()
if __name__=="__main__":
    menu()