import mysql.connector
import json
import os
from tabulate import tabulate

def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="practicedb"
    )
    mycursor = mydb.cursor()
    return mydb, mycursor

def table():
    db, cur = connection()
    tb = input("Enter the table name: ").strip()
    c_no = int(input(f"Enter the no. of columns for {tb}: "))
    column = ["id int auto_increment primary key"]
    for i in range(c_no):
        c_name = input(f"Enter the name for column {i+1}: ").strip()
        c_type = input(f"Enter the types for {c_name} (e.g. varchar(100), int, date): ").strip()
        column.append(f"{c_name} {c_type}")
    sql = f"CREATE TABLE IF NOT EXISTS {tb}({', '.join(column)})"
    cur.execute(sql)
    db.commit()
    print(f" Table '{tb}' created successfully!")
    cur.close()
    db.close()

def insert():
    db, cur = connection()
    tb = input("Enter the table name: ").strip()
    cur.execute(f"DESC {tb}")
    cols = [col[0] for col in cur.fetchall() if col[0] != 'id']

    values = []
    for col in cols:
        val = input(f"Enter value for {col}: ")
        values.append(val)

    p_holder = ','.join(['%s'] * len(cols))
    sql = f"INSERT INTO {tb}({','.join(cols)}) VALUES ({p_holder})"
    cur.execute(sql, values)
    db.commit()
    print(f" Data inserted successfully into '{tb}'!")
    cur.close()
    db.close()

def select():
    db, cur = connection()
    tb = input("Enter the table name: ").strip()
    cur.execute(f"SELECT * FROM {tb}")
    rows = cur.fetchall()

    cur.execute(f"DESC {tb}")
    cols = [col[0] for col in cur.fetchall()]
    # print(f"Columns: {', '.join(cols)}\n")
    
    tbl=tabulate(rows,headers=cols, tablefmt="github")
    print(tbl)
    
    # for row in rows:
    #     print(row)

    cur.close()
    db.close()

def delete():
    db, cur= connection()
    tb=input("Enter the table name: ").strip()
    cur.execute(f"select * from {tb}")
    rows=cur.fetchall()

    cur.execute("desc {tb}")
    cols=[col[0] for col in cur.fetchall()]

    tbl=tabulate(rows,headers=cols, tablefmt="github")

    print(tbl)

    d=input("Enter the column name to delete: ")
    v=input("Enter the value to delete: ")
    val=(d,v)
    sql="delete from {tb} where %s=%s"

    cur.execute(sql,val)

    print(f"Successfully deleted. {v} from {d}")

    db.commit()
    cur.close()
    db.close()


def export_to_json():
    db, cur = connection()
    tb = input("Enter the table name to export: ").strip()

    cur.execute(f"SELECT * FROM {tb}")
    rows = cur.fetchall()

    cur.execute(f"DESC {tb}")
    cols = [col[0] for col in cur.fetchall()]

    data_list = [dict(zip(cols, row)) for row in rows]

    folder = "json_exports"
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, f"{tb}.json")
    with open(file_path, "w") as f:
        json.dump(data_list, f, indent=4)

    print(f" Data from '{tb}' exported successfully to '{file_path}'")
    cur.close()
    db.close()


while True:
    print("\n1. Create Table\n2. Insert Data\n3. View Table\n4. Export to JSON\n5. Delete Data\n6. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        table()
    elif choice == '2':
        insert()
    elif choice == '3':
        select()
    elif choice == '4':
        export_to_json()
    elif choice == '5':
        delete()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Try again!")
