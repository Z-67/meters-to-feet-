import wx
from backend import meters_feet

#function for when convert button is pressed 
def press_button(event):
    meters = float(input_box.GetValue()) # Get the value from the input text box
    result.SetLabel(str(meters_feet(meters))) #Call the meters_feet function from the backend program and set it to result label

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

# Bind the press_button function to the button's click event
button.Bind(wx.EVT_BUTTON, press_button)

# Adds grid positions by putting in row and column
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
