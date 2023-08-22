import PySimpleGUI as sg

layout = [
        [sg.Text('\n\nInitialization\n',expand_x=True,pad=(10,10),justification='center')],
        [sg.ProgressBar(max_value=100, orientation='h', size=(50, 30),expand_x=True)],
        [sg.Text('Finding Sycra Elf...',expand_x=True,justification='center')],
        [
            sg.Button('Testing Click' )
        ]
    
]


window = sg.indow("sam test", layout, resizable=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # Handle events and values here

# Close the window
window.close()