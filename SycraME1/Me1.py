import PySimpleGUI as sg

# Define the layout

frame1_layout = [
    [sg.Text('Grouping', font=('Helvetica', 20 ))],
    #list with dummy data 
    [sg.Multiline(size=(30, 6)) ],
    #button
    [sg.Button('Add')]
]

# layout = [
#     [sg.Column([
#         [sg.Frame("group added", frame1_layout, expand_x=True, expand_y=True, background_color='#0083e6')]
#     ],expand=True)]

# ]

layout = [
    [sg.Column([ 
        [sg.Frame("group", frame1_layout, expand_x=True, expand_y=True,  background_color='#0083e6')]
    ])]
]

window = sg.Window('SycraME', layout, resizable=True)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Add':
        # Add your code here for what happens when the button is clicked
        pass

# Close the window
window.close()