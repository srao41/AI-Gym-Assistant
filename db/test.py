#!/usr/bin/python

import sqlite3

# # c.execute(""" CREATE TABLE rep_counter (
# #         start_time text,
# #         end_time text,
# #         date text,
# #         left int,
# #         right int,
# #         total int
# # )""")


def add(start_time,end_time,date,left,right,total):
    db_path = "db/rep.db"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("INSERT INTO rep_counter VALUES (?,?,?,?,?,?)",(start_time,end_time,date,left,right,total))
    conn.commit()
    conn.close()

def show_all():
    db_path = "db/rep.db"
    conn = sqlite3.connect(db_path)
    c= conn.cursor()

    #query the db
    c.execute('SELECT rowid,* FROM rep_counter')

    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()    
    conn.close()

def delete_row(row_no):
    db_path = "db/rep.db"
    conn = sqlite3.connect(db_path)
    c= conn.cursor()

    c.execute("DELETE from rep_counter WHERE rowid = {}".format(row_no))    

    conn.commit()    
    conn.close()
