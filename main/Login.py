#! /usr/bin/python3
# -*- coding:utf-8 -*-

import wx
import main

message = ""


class Frame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(
            self, parent, id, title='爱尚花艺营销管理系统', pos=(
                450, 200), size=(
                300, 200))
        icon = wx.Icon('../src/images/ishy.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)  # 设置Frame标题的图标
        panel = wx.Panel(self)

        self.title = wx.StaticText(panel, label='请输入用户名和密码')
        self.font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.label_user = wx.StaticText(panel, label='用户名:')
        self.text_user = wx.TextCtrl(panel, size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密  码:')
        self.text_pwd = wx.TextCtrl(
            panel, size=(235, 25), style=wx.TE_PASSWORD)
        self.bt_confrim = wx.Button(panel, label='OK')
        self.bt_confrim.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='cancel')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)

        h_user = wx.BoxSizer(wx.HORIZONTAL)
        h_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        h_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        h_pwd = wx.BoxSizer(wx.HORIZONTAL)
        h_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        h_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)
        h_button = wx.BoxSizer(wx.HORIZONTAL)
        h_button.Add(self.bt_confrim, proportion=0, flag=wx.ALL, border=5)
        h_button.Add(self.bt_cancel, proportion=0, flag=wx.ALL, border=5)

        v_all = wx.BoxSizer(wx.VERTICAL)
        v_all.Add(self.title, proportion=0, flag=wx.BOTTOM |
                  wx.TOP | wx.ALIGN_CENTER, border=15)
        v_all.Add(h_user, proportion=0, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=45)
        v_all.Add(h_pwd, proportion=0, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=45)
        v_all.Add(h_button, proportion=0,
                  flag=wx.ALIGN_CENTER | wx.TOP, border=15)

        panel.SetSizer(v_all)

    def OnclickSubmit(self, event):  # 设置点击确定事件
        global message
        username = self.text_user.GetValue()
        password = self.text_pwd.GetValue()
        if username == "" or password == "":
            message = "用户名或密码不能为空"
        elif username == 'lm' and password == '111':
            frame.Close()
            main.Frame.ShowMain()
        else:
            message = '用户名或密码错误'
        if message == '登录成功':
            wx.MessageBox(message)
        else:
            wx.MessageBox(message)

    def OnclickCancel(self, event):  # 设置点击取消事件
        self.text_user.SetValue('')
        self.text_pwd.SetValue('')


if True:
    app = wx.App()
    frame = Frame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
