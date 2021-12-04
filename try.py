from tkinter import *
from tkinter import ttk
from datetime import datetime
import os
import csv

root = Tk()
root.title("TRY")
root.geometry("1200x600")
root.resizable(True, True)

tframe = Frame(root)
tframe.place(x=0, y=285, height=300, width=500)

table = ttk.Treeview(root)
table.place(x=0, y=285, height=150, width=450)
table_scroll = ttk.Scrollbar(root, orient="vertical", command=table.yview)
table_scroll.place(x=450, y=285, height=150)
table.configure(yscrollcommand=table_scroll.set)

table['columns'] = ('File', 'Datetime')

table.column('#0', width=0, stretch=NO)
table.column("File", anchor=W, width=200)
table.column("Datetime", anchor=W, width=140)

table.heading("#0", text="")
table.heading("File", text="File", anchor=W)
table.heading("Datetime", text="Datetime", anchor=W,
              command=lambda: tree_view_sort_column(table, "Datetime"))

date_time1 = "12/12/2021 14:54"
date_time2 = "12/11/2021 13:30"
date_time3 = "12/01/2021 12:24"
date_time4 = "23/05/2021 10:00"
date_time5 = "23/05/2021 10:01"


def tree_view_sort_column(tv, col):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(key=lambda x: datetime.strptime(x[0], '%d/%m/%Y %H:%M'))

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)


'''f = open("Upload_file_try.txt", "w")

item_id1 = table.insert(parent='', index='end', values=("Quinto", date_time1))
values1 = table.item(item_id1)['values']
for element in values1:
    f.write(element + " ")
f.write("\n")

item_id2 = table.insert(parent='', index='end', values=("Quarto", date_time2))
values2 = table.item(item_id2)['values']
for element in values2:
    f.write(element + " ")
f.write("\n")

item_id3 = table.insert(parent='', index='end', values=("Primo", date_time3))
values3 = table.item(item_id3)['values']
for element in values3:
    f.write(element + " ")
f.write("\n")

item_id4 = table.insert(parent='', index='end', values=("Secondo", date_time4))
values4 = table.item(item_id4)['values']
for element in values4:
    f.write(element + " ")
f.write("\n")

item_id5 = table.insert(parent='', index='end', values=("Terzo", date_time5))
values5 = table.item(item_id5)['values']
for element in values5:
    f.write(element + " ")

tree_view_sort_column(table, "Datetime")

f.close()'''

'''with open("Upload_file_try.txt") as my_file:
    while True:
        try:
            line = my_file.readline().split(None)[1]
        except IndexError:
            break
        print(line)
'''


def remove_file():
    global item, item_text
    print("selected items: ")
    for item in table.selection():
        print(item)
        print(table.selection())
        item_text = table.item(item, 'values')[0]
        print(item_text)
        table.delete(item)
    with open("Upload_file_try.txt", "r") as my_file:
        lines = my_file.readlines()
        print(lines)
    with open("Upload_file_try.txt", "w")as my_file:
        for line in lines:
            print(line.split(sep=None)[0].strip())
            if line.split(sep=None)[0].strip() != item_text:
                my_file.write(line)


def save():
    with open("new_try.csv", "w", newline='')as my_file:
        csv_writer = csv.writer(my_file, delimiter=',')

        for row_id in table.get_children():
            row = table.item(row_id)['values']
            print('save row: ', row)
            csv_writer.writerow(row)


def load():
    with open("new_try.csv") as my_file:
        csv_read = csv.reader(my_file, delimiter=',')

        for row in csv_read:
            print('load row: ', row)
            table.insert("", 'end', values=row)


remove = Button(root, text="Remove", command=remove_file)
remove.place(x=480, y=285, height=50, width=150)

save = Button(root, text="Save", command=save)
save.place(x=480, y=200, height=50, width=100)

load = Button(root, text="Load", command=load)
load.place(x=480, y=150, height=50, width=100)
root.mainloop()
