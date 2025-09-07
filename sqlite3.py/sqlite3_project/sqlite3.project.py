# Before running this program install tabulate lib.
import sqlite3
import json
import csv
import os
from tabulate import tabulate as t

db_name = ''

def connection():
  global db_name
  if not db_name:
    db_name = input("Enter the DB name (with extension .db): ").strip()
  db = sqlite3.connect(f"{db_name}")
  cur = db.cursor()
  return db, cur

def c_table():
  db, cur = connection()
  tb = input('Enter the name of new table: ')
  clm = int(input(f"Enter the no. of column for {tb}: "))
  columns = ["id integer primary key autoincrement"]
  for i in range(clm):
    c_name = input(f"Enter the name for column {i+1}: ")
    c_type = input(f"Enter the type for the {c_name}: ")
    columns.append(f"{c_name} {c_type}")
  column = ', '.join(columns)

  sql = f"create table if not exists {tb} ({column})"
  cur.execute(sql)

  db.commit()

  print("Table created successfully")
  cur.close()
  db.close()

def s_table():
  db, cur = connection()
  tb = input("Enter the table name: ")
  try:
    cur.execute(f"select * from {tb}")
  except sqlite3.OperationalError as e:
    print('Error: ', e)
    cur.close()
    db.close()
    return 

  rows = cur.fetchall()
  cols = [col[0] for col in cur.description]
  tbl = t(rows, headers=cols, tablefmt='github')
  print(tbl)
  cur.close()
  db.close()

def i_table():
  db, cur = connection()
  tb = input("Enter the name of the table: ")

  cur.execute(f"pragma table_info({tb})")
  col_i = cur.fetchall()
  cols = [col[1] for col in col_i if col[5] == 0]

  print(f"The available columns are {cols}")
  n = int(input("How many rows do you want to insert? :"))
  values = []
  for i in range(n):
    value = []
    for col in cols:
      c_1 = input(f"Enter the data for {col}")
      value.append(c_1)
    values.append(value)

  p_holder = ','.join(['?'] * len(cols))
  sql = f"insert into {tb} ({', '.join(cols)}) values({p_holder})"
  cur.executemany(sql, values)

  db.commit()
  print(f"\n {n} row(s) inserted successfully into {tb}!")

  cur.close()
  db.close()

def j_export():
  db, cur = connection()
  tb = input("Enter the table name: ")

  cur.execute(f"select * from {tb}")
  rows = cur.fetchall()
  cols = [col[0] for col in cur.description]
  data = [dict(zip(cols, row)) for row in rows]

  folder = input("Enter the folder name: ")
  if not os.path.exists(folder):
    os.makedirs(folder)

  j_file = input("Enter the Json file name with extension(.json): ")
  f_join = os.path.join(folder, j_file)

  with open(f_join, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

  print("json file exported successfully.")
  cur.close()
  db.close()

def c_export():
  db, cur = connection()
  tb = input("Enter the table name: ")
  cur.execute(f"select * from {tb}")
  rows = cur.fetchall()
  cols = [col[0] for col in cur.description]

  c_file = input("Enter the name of the csv file with extension(.csv): ")
  with open(c_file, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(cols)
    w.writerows(rows)
  print(f"CSV file saved successfully as {c_file}")

  cur.close()
  db.close()

# Main Menu
while True:
  print("\n--- SQLite Manager ---")
  print("1. Create Table")
  print("2. Show Table")
  print("3. Insert Into Table")
  print("4. Export Table to JSON")
  print("5. Export Table to CSV")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ").strip()

  if choice == '1':
    c_table()
  elif choice == '2':
    s_table()
  elif choice == '3':
    i_table()
  elif choice == '4':
    j_export()
  elif choice == '5':
    c_export()
  elif choice == '6':
    print("Exiting program. Bye!")
    break
  else:
    print("Invalid choice. Please enter a number between 1-6.")
