import mysql.connector

def connection():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="practicedb"
        )
    mycursor=mydb.cursor()
    return mydb, mycursor

def table():
    db,cur=connection()
    tb = input("Enter the table name: ").strip()
    c_no=int(input(f"Enter the no. of column for {tb}: "))
    column=["id int auto_increment primary key"]
    for i in range(c_no):
        c_name=input(f"Enter the name for column {i+1}")
        c_type=input(f"Enter the types for {c_name} (e.g. varchar(100), int, date): ")
        column.append(f"{c_name} {c_type}")
    sql=(f"create table if not exists {tb}({', '.join(column)})")
    cur.execute(sql)
    db.commit()
    print("Table created successfully:")
    cur.close()
    db.close()

def insert():
    db, cur=connection()
    tb = input("Enter the table name: ").strip()
    cur.execute(f"desc {tb}")
    cols=[col[0] for col in cur.fetchall() if col[0] !='id']

    values=[]
    for col in cols:
        val=input(f"Enter values for {col}: ")
        values.append(val)

    p_holder=','.join(['%s']*len(cols))

    sql=(f"insert into {tb}({','.join(cols)}) values ({p_holder})")
    cur.execute(sql, values)

    db.commit()
    cur.close()
    db.close()

def select():
    db, cur=connection()
    tb = input("Enter the table name: ").strip()
    cur.execute(f"select * from {tb}")
    rows=cur.fetchall()

    cur.execute(f"desc {tb}")
    cols=[col[0] for col in cur.fetchall()]
    print(f"Columns: {','.join(cols)}\n")

    for row in rows:
        print(row)

    cur.close()
    db.close()


while True:
    print("\n1. Create Table\n2. Insert Data\n3. View Table\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        table()
    elif choice == '2':
        insert()
    elif choice == '3':
        select()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Try again!")