import wx
from backend import meters_feet

# Create a wxPython application object
app = wx.App(False)

# Create window for application
frame = wx.Frame(parent=None, title="Meters to feet")

# Container within frame to group content
panel = wx.Panel(frame)

# allows you to put things in certain columns and rows
sizer = wx.GridBagSizer()

# Create labels, input box, and result display
input_label = wx.StaticText(panel, label="Meters: ")
input_box = wx.TextCtrl(panel)
result_label = wx.StaticText(panel, label="Feet: ")
result = wx.StaticText(panel, label="")

# Create a button for conversion
button = wx.Button(panel, label="Convert")

# Adds grid positions
sizer.Add(input_label, (0, 0))
sizer.Add(input_box, (0, 1))
sizer.Add(result_label, (1, 0))
sizer.Add(result, (1, 1))
sizer.Add(button, (2, 0))

# allows labels/boxes to be positioned
panel.SetSizer(sizer)

# Show the frame
frame.Show()

# Start the wxPython event loop
app.MainLoop()
