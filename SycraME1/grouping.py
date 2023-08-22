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
lis = []
# define right column layout
right_column_layout = [
    [
        sg.Text('Groud Added:', font=('Helvetica', 18), text_color='black')
    ],
    [
        sg.Text('List of scanned devices:', font=('Helvetica', 12), text_color='black')
    ],
       [
        sg.Input(key='-INPUT-', enable_events=True),
        sg.Button('Add', key='-ADD-', button_color=('#ffffff', '#0083e6'))
    ],

     [
        # list box  data
        
         sg.Listbox(values=[''], key='-LIST-', size=(30,4),
                    background_color='#999999')
     ],
  
    
    # add button 
    [
        sg.Button('Add', button_color=('#ffffff', '#0083e6'))
    ]
]

# defined main layout
layout = [
    [
        sg.Column(left_column_layout, element_justification='center', background_color='#0083e6', size=(200, None)),
        sg.Column(right_column_layout, element_justification='center', size=(600, None))
    ]
]

# create the window
window = sg.Window('SycraMe', layout, resizable=True)

# Run the event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-ADD-':
        # Get the entered text
        text = values['-INPUT-']
        # Validate the entered text using a regular expression
        if re.match(r'^\S+$', text):
            # Add the entered text to the list
            window['-LIST-'].update(values['-LIST-'] + [text])
            # Clear the input field
            window['-INPUT-'].update('')
        else:
            # Display an error message
            sg.popup('Error: Please enter a single word without spaces.')

window.close()