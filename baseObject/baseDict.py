#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 19:33
# @Author  : Fuxl
# @Site    : 
# @File    : baseDict.py
# @Software: PyCharm

baseDict_help = {
#返回字典元素
'values':       'dict.values()以列表返回字典中的所有值',
'keys':         'dict.keys()  以列表返回一个字典所有的键',
'items':        'dict.items() 以列表返回可遍历的(键, 值) 元组数组',
'get':          'dict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值',
'clear':        'dict.clear()删除字典内所有元素 ',
'fromkeys':    'dict.fromkeys(seq[, val]) 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值,eg:dict.fromkeys(baseDict_help.keys(),1)',
'setdefault':   'dict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default',
'pop':          'pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。',
'popitem':      'popitem()随机返回并删除字典中的一对键和值。',
'update':       'dict.update(dict2)把字典dict2的键/值对更新到dict里',

'copy':         'dict.copy() 返回一个字典的浅复制',
}

def test():
    #values keys items
    print(baseDict_help.values())
    print(baseDict_help.keys())
    print(baseDict_help.items())

    baseDict_help.clear()
    print(baseDict_help)

    baseDict_help.setdefault('test')
    baseDict_help.setdefault('test1',1)
    baseDict_help.setdefault('test2',"test")
    print(baseDict_help)

    print("get test3:",baseDict_help.get('test3','not the keys'))
    print("fromkeys:",dict.fromkeys(baseDict_help.keys()))
    print("fromkeys:",dict.fromkeys(baseDict_help.keys(), 2))

    baseDict_help.pop('test')
    print('pop:',baseDict_help)

    baseDict_help.popitem()
    print('popitem:', baseDict_help)

    dtt = {}
    dtt.update(baseDict_help)
    print('update:', dtt)




