
# coding = utf-8


# 这是一个打卡计时器


import tkinter
import pymysql
from tkinter.constants import GROOVE, DISABLED
from distutils.cmd import Command
from _tkinter import create

# gui部分
root = tkinter.Tk()

def outputletter():
    print('out')

start = tkinter.Button(root,text='a')

tkinter.Button(root, text="外观装饰边界附近的标签", width=19,relief=GROOVE,bg="red").pack()

tkinter.Button(root, text="设置按钮状态",width=21,state=DISABLED).pack()

tkinter.Button(root, text = "输出文本", command = outputletter).pack()

tr_text = tkinter.Text(root)
tr_text.insert(1.0, '这个是可输入的文本框')
tr_text.pack()

tr_label = tkinter.Label(root,text='本周已工作')
tr_label.pack()

start.pack()

# root.mainloop()


# 数据库部分

host = '127.0.0.1'
user = 'root'
password = 'root'
db_list = []
tb_list =[]

dbcon = pymysql.connect(host,user,password)
cur = dbcon.cursor()

def check_db():
    cur.execute("show databases")
    for db in cur.fetchall():
        db_list.append(db[0])
    return db_list

def check_tb(db):
    cur.execute("use %s" %db)
    cur.execute("select database()")
    print ("当前数据库： %s" %cur.fetchall()[0])
    all_table = cur.execute("show tables")
    for tb in cur.fetchall():
        tb_list.append(tb[0])
    return tb_list
def creat_db():



a = check_db()
print (a)
b = create_db(db_list)
print b
c = check_tb(b)
print (c)


