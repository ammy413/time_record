
# coding = utf-8


# 这是一个打卡计时器


import tkinter
from tkinter.constants import GROOVE, DISABLED
from distutils.cmd import Command

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

root.mainloop()

