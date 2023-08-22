import PySimpleGUI as sg
import re

#set the theme
sg.theme('LightBlue1')

# define column layout 

left_column_layout = [
    [
        sg.Text('SycraMe', justification='center', font=('Helvetica', 18),
                text_color='white', background_color='#0083e6')
    ],
    #buttons
    [sg.Button('Discover', size=(10, 1))],
    [sg.Button('Grouping', size=(10, 1))],
    [sg.Button('Settings', size=(10, 1))]
]

right_column_layout = [
     # right column header
    [
        sg.Text('Groud Added:', font=('Helvetica', 18), text_color='black')
    ],

    #mini devices scanned header
    [
        sg.Text('List of scanned devices:', font=('Helvetica', 12), text_color='black')
    ],

      [
        # multiline input box data
        
         sg.Multiline(key='-MULTILINE-', size=(30,4), background_color='#999999', enable_events=True, autoscroll=True)
     ]
]

# defined main layout
layout = [
    [
        sg.Column(left_column_layout, element_justification='center', background_color='#0083e6', size=(200, None)),
        sg.Column(right_column_layout, element_justification='center', size=(600, None))
    ]
]

# Create the window with a white background color
window = sg.Window('SycraME', layout, resizable=True)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-MULTILINE-':
        # Get the current value in the multiline input box
        current_value = values['-MULTILINE-']
        
        # Split the value into lines
        lines = current_value.split('\n')
        
        # Check if the last line is longer than 33 characters
        if len(lines[-1]) > 40:
            # Insert a newline character after every 33 characters in the last line
            new_line = '\n'.join([lines[-1][i:i+40] for i in range(0, len(lines[-1]), 40)])
            
            # Update the value in the multiline input box with the new line
            window['-MULTILINE-'].update('\n'.join(lines[:-1] + [new_line]))
    
window.close()

