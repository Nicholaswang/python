#first wxwindows app
import wx

app=wx.PySimpleApp()
frame=wx.Frame(None,-1,"First Windows",size=(300,300))
frame.Show(True)

app.MainLoop()
