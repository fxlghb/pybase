#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk

class tkinterLogin:
    var_usr_name = tk.StringVar()
    var_usr_pwd = tk.StringVar()

    def __init__(self):
        pass

    def usr_init():
        global var_usr_name
        global var_usr_pwd
        var_usr_name.set('example@python.com')
        print('test user_init')

    def usr_login():
        pass
    
    def usr_sign_up():
        exit()