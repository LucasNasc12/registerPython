import tkinter as tk
import sqlite3
import pandas as pd

# # create database
# connection = sqlite3.connect('clientes.db')
#
# # create cursor
# curs = connection.cursor()
#
# # create table
#
# curs.execute(""" CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )""")
#
# # commit as mudanças
# connection.commit()
#
# # close db
# connection.close()

# window
window = tk.Tk()
window.title('Cadastro de clientes')
window.geometry("330x350")

def register_clients():
    connection = sqlite3.connect('clientes.db')
    curs = connection.cursor()

    #insert data on table
    curs.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)",
                 {
                     'nome': entry_name.get(),
                     'sobrenome': entry_lastname.get(),
                     'email': entry_email.get(),
                     'telefone': entry_phone.get()
                 })


    #commit as mudanças:
    connection.commit()

    #close db
    connection.close()

    #delete entry box
    entry_name.delete(0,"end")
    entry_lastname.delete(0,"end")
    entry_email.delete(0,"end")
    entry_phone.delete(0,"end")

def export_clients():
    connection = sqlite3.connect('clientes.db')
    curs = connection.cursor()

    #Insert data on table:
    curs.execute("SELECT *, oid FROM clientes ")
    registered_clients = curs.fetchall()
    #print(registered_clients)
    registered_clients=pd.DataFrame(registered_clients,columns=['nome','sobrenome','email','telefone','Id_banco'])
    registered_clients.to_excel('clientes.xlsx')

    connection.commit()
    connection.close()




#entrys
label_name = tk.Label(window, text='Name')
label_name.grid(row=0, column=0, padx=10, pady=10)

label_lastname = tk.Label(window, text='Last Name')
label_lastname.grid(row=1, column= 0, padx=10, pady=10)

label_email = tk.Label(window, text='E-Mail')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_phone = tk.Label(window, text= 'Phone')
label_phone.grid(row=3, column=0, padx=10, pady=10)

#box entrys
entry_name = tk.Entry(window, width=35)
entry_name.grid(row= 0, column=1, padx=10, pady=10)

entry_lastname = tk.Entry(window, width=35)
entry_lastname.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(window, width=35)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_phone = tk.Entry(window, width=35)
entry_phone.grid(row=3, column=1, padx=10, pady=10)

# button register
button_register = tk.Button(text='Register client', command=register_clients)
button_register.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

#button export
button_export = tk.Button(text='Export to Excel', command=export_clients)
button_export.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

window.mainloop()