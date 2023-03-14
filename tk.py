import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sqlite3
import datetime

window = tk.Tk()
window.title("Daily blinking")
window.geometry('1280x800')
#window.minsize(800,600)
#window.maxsize(1800,1600)

frame_up = tk.Frame(window) #bg='green' 
frame_down = tk.Frame(window) #bg='blue'

frame_up.pack(side='top',fill='both',expand=True)
frame_down.pack(side='bottom', fill='both', expand=True)

l_zip_text=tk.Label(frame_up, text = 'Rigion')
l_zip_search=tk.Entry(frame_up)                                         #Вставить в запрос, если пусто = *
l_hostname_text=tk.Label(frame_up, text = 'BS')
l_hostname_search=tk.Entry(frame_up)                                    #Вставить в запрос, если пусто = *
l_firstoccurrence_text=tk.Label(frame_up, text = 'Date')
l_firstoccurrence_search=tk.Entry(frame_up)                             #Вставить в запрос, если пусто = *
l_eventid_text=tk.Label(frame_up, text = 'Alarm')
l_eventis_search=tk.Entry(frame_up)                                     #Вставить в запрос, если пусто = *

l_zip_text.grid(row="0",column="0",padx=10,pady=10)
l_zip_search.grid(row="0",column="1",padx=10,pady=10)
l_hostname_text.grid(row="1",column="0",padx=10,pady=10)
l_hostname_search.grid(row="1",column="1",padx=10,pady=10)
l_firstoccurrence_text.grid(row="2",column="0",padx=10,pady=10)
l_firstoccurrence_search.grid(row="2",column="1",padx=10,pady=10)
l_eventid_text.grid(row="3",column="0",padx=10,pady=10)
l_eventis_search.grid(row="3",column="1",padx=10,pady=10)

table = ttk.Treeview(frame_down)
heads =['id','zip','site','hostname','first','end','severity','eventid','info']
table['columns'] = heads
all_data =[]

table.column("#1",width=50)
table.column("#2",width=70)
table.column("#3",width=100)
table.column("#4",width=100)
table.column("#5",width=150)
table.column("#6",width=150)
table.column("#7",width=50)
table.column("#8",width=150)

with sqlite3.connect('9-3.db') as db:
    cursor=db.cursor()
    query = """SELECT * FROM alarm_daily limit 10"""                    #where zip = '...' and hostname = '...' and firstoccurrence like '...%' and eventid = '...'
    cursor.execute(query)
    all_data=cursor.fetchall()

for header in heads:
    table.heading(header,text=header,anchor='center')
    table.column(header,anchor='center')

scroll=ttk.Scrollbar(frame_down, command=table.yview)
table.configure(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

for row in all_data:
    table.insert('',tk.END,values=row)

table.pack(expand=tk.YES, fill='both')

# Button
button = tk.Button(frame_up, text="Enter data")
button.grid(row=5, column=0, padx=50, pady=10)

def search(l_zip_search="", l_hostname_search="", l_firstoccurrence_search="", l_eventis_search=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes WHERE zip=? and hostname=? and firstoccurrence=? and eventid=?", (zip,hostname,firstoccurrence, eventid))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def clicked():  
    button.configure(text="update")
    all_data =[]
    with sqlite3.connect('9-3.db') as db:
        cursor=db.cursor()
        query = """SELECT * FROM alarm_daily limit 50"""
        cursor.execute(query)
        all_data=cursor
    #return all_data

window.mainloop() #Эта функция вызывает бесконечный цикл окна
