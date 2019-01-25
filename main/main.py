#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
sys.path.append("../lib/")
import MenuLib
import Login
import wx
from Login import message       #导入Login包里的message变量

Login       #调用登录界面

class Frame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,title='爱尚花艺营销管理系统',pos=(135,25),size=(1024,700))   #窗口定义
		icon = wx.Icon('../images/ishy.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon)      #设置Frame标题的图标
		panel = wx.Panel(self)      #创建画板容器
		self.menubar = wx.MenuBar()     #新建菜单栏
		self.menu1 = wx.Menu()      #新建菜单1
		self.menubar.Append(self.menu1,'商品管理')        #将menu1加入菜单栏并命名

		self.menuitem11 = self.menu1.Append(wx.ID_NEW,"新建")      #新加入一个menuitem11并命名
		self.Bind(wx.EVT_MENU,MenuLib.OnClickMenu11,self.menuitem11)
		self.menu1.AppendSeparator()

		self.menuitem12 = self.menu1.Append(wx.ID_NEW,'打开')
		self.Bind(wx.EVT_MENU,MenuLib.OnClickMenu12,self.menuitem12)
		self.menu1.AppendSeparator()

		self.menuitem13 = self.menu1.Append(wx.ID_NEW,'编辑')      #新加入一个menuitem13并命名
		self.Bind(wx.EVT_MENU,MenuLib.OnClickMenu13,self.menuitem13)

		self.menu2 = wx.Menu()
		self.menubar.Append(self.menu2,'进货管理')

		self.menuitem21 = self.menu2.Append(wx.ID_NEW,'新建')
		self.Bind(wx.EVT_MENU,MenuLib.OnClickMenu21,self.menuitem21)
		self.menu2.AppendSeparator()

		self.menuitem22 = self.menu2.Append(wx.ID_NEW,'打开')
		self.Bind(wx.EVT_MENU,MenuLib.OnClickMenu22,self.menuitem22)
		self.menu2.AppendSeparator()

		self.menuitem23 = self.menu2.Append(wx.ID_NEW,'编辑')      #新建一个menuitem23并命名
		self.Bind(wx.EVT_MENU,MenuLib.OnClickMenu23,self.menuitem23)      #绑定事件

		self.SetMenuBar(self.menubar)   #将菜单栏加入窗口


while True:
	if message == '登录成功':
		app = wx.App()          
		frame = Frame(parent=None,id=-1)            
		frame.Show()            
		app.MainLoop()
	break