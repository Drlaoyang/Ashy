#coding:utf-8

import Login
import wx
from Login import message       #导入Login包里的message变量

Login       #调用登录界面

class Frame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='爱尚花艺营销管理系统',pos=(135,25),size=(1024,700))   #窗口定义
        icon = wx.Icon('..\images\ishy.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon) #设置Frame标题的图标
        panel = wx.Panel(self)  #创建画板容器
        #########################################
        self.menubar = wx.MenuBar()
        self.menuNew = wx.Menu()
        self.menubar.Append(self.menuNew,'商品')
        self.menuitem1 = wx.MenuItem(id=wx.NewId(),text='新建')
        self.menuNew.Append(self.menuitem1)
        self.SetMenuBar(self.menubar)
        #########################################
    
    def hi(self,event):
        print('Hello')
    
while True:
    if message == '登录成功':
        app = wx.App()          
        frame = Frame(parent=None,id=-1)            
        frame.Show()            
        app.MainLoop()
    break