#! /usr/bin/python3
# -*- coding:utf-8 -*-
import sqlite3

connect = sqlite3.connect("../src/databases/database.db")
cursor = connect.cursor()


def OnClickMenu11(event):  # menu11新建事件
    global connect, cursor
    print("Hello World")


def OnClickMenu12(event):  # menu12打开事件
    global connect, cursor
    print("Hello World")


def OnClickMenu13(event):  # menu13编辑事件
    global connect, cursor
    print("Hello World")


def OnClickMenu21(event):  # menu21新建事件
    global connect, cursor
    print("Hello World")


def OnClickMenu22(event):  # menu22打开事件
    global connect, cursor
    print("Hello World")


def OnClickMenu23(event):  # menu23编辑事件
    global connect, cursor
    print("Hello World")
