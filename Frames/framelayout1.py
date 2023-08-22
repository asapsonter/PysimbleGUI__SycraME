import PySimpleGUI as sg

# Define the layouts for each frame
frame1_layout = [
    [sg.Text("frame 1")],
    [sg.Input(key="-IN-")],
    [sg.Button("Bt1")]
]

frame2_layout = [
    [sg.Text("frame 2")],
    [sg.Checkbox("Option 1"), sg.Checkbox("Option 2")],
    [sg.Button("Bt1")]
]

frame3_layout = [
    [sg.Text("frame 3")],
    [sg.Radio("Choice 1", "RADIO1"), sg.Radio("Choice 2", "RADIO1")],
    [sg.Button("Bt3")]
]

frame4_layout = [
    [sg.Text("frame 4")],
    [sg.Radio("Choice 1", "RADIO1"), sg.Radio("Choice 2", "RADIO1")],
    [sg.Button("Bt4")]
]

# define the main layout using columns and frames
layout = [
    [sg.Column([
        [sg.Frame("Frame 1", frame1_layout, expand_x=True, expand_y=True )],
        [sg.Frame("frame 2", frame2_layout, expand_x=True, expand_y=True)]
    
    ],  expand_x=True, expand_y=True),
    sg.VSeparator(),
    sg.Column([
        [sg.Frame("Frame 3", frame3_layout, expand_x=True, expand_y=True)]
    ],expand_x=True, expand_y=True )],

    [sg.Column([
        [sg.Frame("frame 4", frame4_layout, expand_x=True, expand_y=True)]
    ], expand_x=True, expand_y=True )]
    
]

# Create the window
window = sg.Window("PySimpleGUI Example", layout, resizable=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # Handle events and values here

# Close the window
window.close()