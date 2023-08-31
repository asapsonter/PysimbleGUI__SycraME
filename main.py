import threading
import PySimpleGUI as sg

# create a window with an input text and a multiline box
layout = [[sg.InputText (key='input')], [sg.Multiline (key='multiline', size=(40, 10))]]
window = sg.Window ('Timer Example', layout)

# define a function that gets the input text and appends it to the multiline box
def update_multiline ():
    # get the input text value
    input_value = window['input'].get ()
    # append it to the multiline box with a newline character
    window['multiline'].update (input_value + "\n", append=True)
    # clear the input text
    window['input'].update ("")
    # create a new timer thread with the same function and interval
    timer = threading.Timer (1.5, update_multiline)
    # start the timer thread
    timer.start ()

# create an initial timer thread with the function and interval
timer = threading.Timer (1.5, update_multiline)
# start the timer thread
timer.start ()

# run the window event loop
while True:
    event, values = window.read ()
    # if the user closes the window, stop the timer and break the loop
    if event == sg.WINDOW_CLOSED:
        timer.cancel ()
        break

# close the window
window.close ()

# def append_input(window, input_value): # Append the input value to the Multiline element
#     window[AllEvt.gpMultilineKey.value].update(input_value + "\n", append=True) # Clear the input field 
#     window[AllEvt.gpInputTextKey.value].update("")

# def handle_events(window):
#     timer = None
#     while True: event, values = window.read()  
#     if event == sg.WIN_CLOSED or event == "Exit":   
#         break 
#     elif event == AllEvt.gpInputTextKey.value:  
#         if timer is not None: timer.cancel() 
#         input_value = values[event] 
#         timer = threading.Timer(1.5, window.write_event_value, args=(“-APPEND-”, input_value)) t
#         imer.start() 
#     elif event == "-APPEND-": 
#         input_value = values[event] append_input(window, input_value)    