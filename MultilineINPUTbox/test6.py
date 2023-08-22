import threading
import PySimpleGUI as sg

# create a window with an input text and a multiline box
layout = [[sg.InputText (key='input')], [sg.Multiline (key='multiline', size=(40, 10))]]
window = sg.Window ('Timer Example', layout)

# define a function that gets the input text and appends it to the multiline box
def update_multiline ():
    # get the input text value
    input_value = window['input'].get ()
    # check if the input value is not empty
    if input_value:
        # append it to the multiline box with a newline character
        window['multiline'].update (input_value + "\n", append=True)
        # clear the input text
        window['input'].update ("")
        # create a new timer thread with the same function and interval
        timer = threading.Timer (1.5, update_multiline)
        # start the timer thread
        timer.start ()

# run the window event loop
while True:
    event, values = window.read ()
    # if the user types something in the input text, call the update_multiline function
    if event == 'input':
        update_multiline ()
    # if the user closes the window, break the loop
    elif event == sg.WINDOW_CLOSED:
        break

# close the window
window.close ()
