#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#15种Tkinter的部件
Button          按钮控件；在程序中显示按钮。
Canvas          画布控件；显示图形元素如线条或文本
Checkbutton     多选框控件；用于在程序中提供多项选择框
Entry           输入控件；用于显示简单的文本内容
Frame           框架控件；在屏幕上显示一个矩形区域，多用来作为容器
Label           标签控件；可以显示文本和位图
Listbox         列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
Menubutton      菜单按钮控件，由于显示菜单项。
Menu            菜单控件；显示菜单栏,下拉菜单和弹出菜单
Message         消息控件；用来显示多行文本，与label比较类似
Radiobutton     单选按钮控件；显示一个单选的按钮状态
Scale           范围控件；显示一个数值刻度，为输出限定范围的数字区间
Scrollbar       滚动条控件，当内容超过可视化区域时使用，如列表框。.
Text            文本控件；用于显示多行文本
Toplevel        容器控件；用来提供一个单独的对话框，和Frame比较类似
Spinbox         输入控件；与Entry类似，但是可以指定输入范围值
PanedWindow     PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
LabelFrame      labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
tkMessageBox    用于显示你应用程序的消息框。
'''

'''
#标准属性;标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。
Dimension       控件大小；
Color           控件颜色；
Font            控件字体；
Anchor          锚点；
Relief          控件样式；
Bitmap          位图；
Cursor          光标；

'''

'''
#管理整个控件区域组织，一下是Tkinter公开的几何管理类：包、网格、位置
pack()      包装；
grid()      网格；
place()     位置；
'''


import tkinter as tk
from tkinterLogin import tkinterLogin as login


def centerWindow(window, width, high):
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2)
    print(size)
    window.geometry(size)

#主体窗体
window = tk.Tk()

#窗口居中
centerWindow(window, 480, 320)
#固定窗口尺寸,禁止改变
window.resizable(False, False)


image_file = tk.PhotoImage(file='image/welcome.gif')#加载图片文件
canvas = tk.Canvas(window, height=120, width=480)#创建画布
image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上
canvas.pack(side='top')#放置画布（为上端）

#标签控件
tk.Label(window,text='用户名：').place(x=50, y=150, width=80, height=40)
tk.Label(window,text='密  码：').place(x=50, y=210, width=80, height=40)

login.usr_init()
#输入框:用户名
tk.Entry(window, textvariable=login.var_usr_name).place(x=160, y=150, width=160, height=40)
#输入框：密码
entry_usr_pwd = tk.Entry(window, textvariable=login.var_usr_pwd, show='*').place(x=160, y=210, width=160, height=40)

#按钮
print('aa',login.var_usr_name)
btn_login = tk.Button(window, text='登陆', command=login.usr_login)#定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=160, y=260, width=60, height=40)
btn_sign_up = tk.Button(window, text='退出', command=login.usr_sign_up)
btn_sign_up.place(x=260, y=260, width=60, height=40)

window.title("login")

window.mainloop()


