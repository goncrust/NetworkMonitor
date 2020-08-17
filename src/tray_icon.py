import wx
import wx.adv


class TaskBar(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBar, self).__init__()
        icon = wx.IconFromBitmap(wx.BitMap('icon.jpeg'))
        self.SetIcon(icon, "Netowrk")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()

        self.rcvItem = wx.MenuItem(menu, -1, "Received")
        self.sntItem = wx.MenuItem(menu, -1, "Sent")

        menu.Append(self.rcvItem)
        menu.AppendSeparator()
        menu.Append(self.sntItem)

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.close()

    def left_down(self):
        return


class MonitorApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBar(frame)
        return True


app = MonitorApp(False)
app.MainLoop()
