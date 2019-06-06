#! /usr/bin/python3
# -*- coding:utf-8 -*-
import sqlite3

global cursor, connect  # 创建全局数据库对象
connect = sqlite3.connect("../src/databases/database.db")  # 实例化对象
cursor = connect.cursor()  # 实例化对象


def OnClickMenu11(event):  # menu11新建事件
    print("Hello World")


def OnClickMenu12(event):  # menu12打开事件
    print("Hello World")


def OnClickMenu13(event):  # menu13编辑事件
    print("Hello World")


def OnClickMenu21(event):  # menu21新建事件
    print("Hello World")


def OnClickMenu22(event):  # menu22打开事件
    print("Hello World")


def OnClickMenu23(event):  # menu23编辑事件
    print("Hello World")
