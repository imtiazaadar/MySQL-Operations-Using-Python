# Imtiaz Adar
# Project : Create, Insert, Update, Delete Operations By MySQL
# Language : Python
# Date : 15/01/2022

import mysql.connector as connector
import os, sys

print('Database Name : ')
dbase_name = input()
global database
database = connector.connect(host='localhost', user='root', password='', database=dbase_name)

# check database is connected or not
def check_database():
    if database is not None:
        print('Connected')
        print()
    else:
        print('Not Connected')
        
# create database if not exists        
def create_database():
    try:
        sql = f"CREATE DATABASE IF NOT EXISTS {dbase_name}"
        cursor.execute(sql)
        print('Database Created Successfully !!!')
        print()
    except Exception:
        print('Database Already Exists !!!')
        
# create table        
def create_table():
    try:
        print('Table Name : ')
        table_name = input()
        print('Columns : ')
        cols = int(input())
        sen = ''
        for _ in range(cols):
            print('Variable Name : ')
            varname = input()
            print('Data Type : ')
            dtype = input()
            print('Space : ')
            space = input()
            print('Null Or Not')
            nullornot = input()
            sen += f"{varname} {dtype}({space}) {nullornot},"
        sen = sen[:len(sen) - 1]
        print('Primary Key : ')
        primary = input()
        sql = f"CREATE TABLE IF NOT EXISTS {table_name}({sen})"
        cursor.execute(sql)
        print('Table Has Created Successfully !!!')
        sql1 = f"ALTER TABLE {table_name} ADD PRIMARY KEY({primary})"
        cursor.execute(sql1)
        print('Primary Key Added !!!')
        print()
    except Exception:
        print('Table Can Not Be Created !!!')

# insert item        
def insert_item():
    print('Table Name : ')
    tab = input()
    print('Rows : ')
    rows = int(input())
    print('Columns : ')
    cols = int(input())
    for _ in range(rows):
        sen = ''
        for _ in range(cols):
            print('Variable Name : ')
            name = input()
            print('Data Type : ')
            dtype = input()
            if dtype.lower() == 'int':
                print(f"{name}'s Value : ")
                val = input()
                sen += f"{val},"
            elif dtype.lower() == 'varchar':
                print(f"{name}'s Value : ")
                val = input()
                sen += f"'{val}',"
            elif dtype.lower() == 'date':
                print('Enter Year : ')
                year = input()
                print('Enter Month : ')
                month = input()
                print('Enter Day : ')
                day = input()
                sen += f"{year}-{month}-{day},"
        sen = sen[:len(sen) - 1]
        try:
            sql = f"INSERT INTO {tab} VALUES({sen})"
            cursor.execute(sql)
            database.commit()
            print('Data Inserted Successfully !!!')
            print()
        except Exception:
            print('Data Can Not Be Inserted !!!')

# update item            
def update_item():
    print('Table Name : ')
    tab = input()
    print('Set Variable : ')
    setvariable = input()
    print('Equals : ')
    eq1 = input()
    print('Where Variable : ')
    where = input()
    print('Equals : ')
    eq2 = input()
    try:
        sql = f"UPDATE {tab} SET {setvariable}='{eq1}' WHERE {where}='{eq2}'"
        cursor.execute(sql)
        database.commit()
        print('Data Updated Successfully !!!')
        print()
    except Exception:
        print('Data Can Not Be Updated !!!')
        
# delete item
def delete_item():
    print('Table Name : ')
    tab = input()
    print('Where Variable : ')
    where = input()
    print('Equals : ')
    eq = input()
    try:
        sql = f"DELETE FROM {tab} WHERE {where}='{eq}'"
        cursor.execute(sql)
        database.commit()
        print('Deleted Successfully !!!')
        print()
    except Exception:
        print('Can Not Be Deleted !!!')

# display table
def display_table():
    print('Table Name : ')
    tab = input()
    try:
        sql = f"SELECT * FROM {tab}"
        cursor.execute(sql)
        c = 0
        size = len(cursor.column_names)
        print(f'\t{tab.upper()} DISPLAYED BELOW   \n')
        for column in cursor.column_names:
            print(column, end='')
            if c < size:
                print('  ||  ', end='')
            c += 1
        print('\n')
        li = []
        for x in cursor:
            li.append(list(x))
        for item in li:
            print(*item, sep='  ||  ')
        print()
    except Exception:
        print('Table Does Not Exist !!!')

# own sql        
def own_sql():
    print('Table Name : ')
    tab = input()
    print('How Many Selects : ')
    how = int(input())
    sen = ''
    if how == 1:
        print('Select Variable : ')
        select = input()
        sen += f'{select}'
    else:
        for _ in range(how):
            print('Select Variable : ')
            select = input()
            sen += f"{select},"
        sen = sen[:len(sen) - 1]
    print('Where Variable : ')
    where = input()
    print('Value : ')
    val = input()
    try:
        query = f"SELECT {sen} FROM {tab} WHERE {where}='{val}'"
        cursor.execute(query)
        c = 0
        size = how
        print(f'\t{tab.upper()} DISPLAYED BELOW   \n')
        for column in cursor.column_names:
            print(column, end='')
            if c < size - 1:
                print('  ||  ', end='')
            c += 1
        print('\n')
        li = []
        for x in cursor:
            li.append(list(x))
        for item in li:
            print(*item, sep='  ||  ')
        print()
        print('Executed Successfully !!!')
        print()
    except Exception:
        print('Can Not Be Executed !!!')
        
# driver
if __name__ == "__main__":
    check_database()
    cursor = database.cursor()
    status = True
    while status:
        print('ENTER YOUR CHOICE\n1. Create Table\n2. Insert\n3. Update\n4. Delete\n5. Own Sql\n6. Display Table\n7. Clear\n8. Exit')
        choice = int(input())
        if choice == 1:
            create_table()
        elif choice == 2:
            insert_item()
        elif choice == 3:
            update_item()
        elif choice == 4:
            delete_item()
        elif choice == 5:
            own_sql()
        elif choice == 6:
            display_table()
        elif choice == 7:
            os.system('cls')
        elif choice == 8:
            status = False
            sys.exit()