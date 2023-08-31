import threading
import PySimpleGUI as sg

# create a window with a multiline box and an input text
layout = [[sg.Multiline(key="-Multi-", enable_events=True, autoscroll=True, size=(60,4),
                    background_color='#999999',  disabled=True )],    
        [sg.InputText(key="-input-", enable_events=True, size=(60, 1))]]
window = sg.Window ('Timer Example', layout)

def updateMultilineBx(window, input_value) :
    window["-Multi-"].update(input_value + "\n", append=True)
    window["-input-"].update("")

# define a function that runs the updateMultilineBx() function with 0.5 second thread
def update_multiline_with_timer (window, input_value): #globalVar: AppGlobal,
    # run the updateMultilineBx() function
    updateMultilineBx(window, input_value)
    # create a new timer thread with the same function and interval
    timer = threading.Timer (0.5, update_multiline_with_timer, args=(window, input_value))
    # start the timer thread
    timer.start ()

# run the window event loop
while True:
    event, values = window.read ()
    # if the user types something in the input text, call the update_multiline_with_timer function
    if event == ["-input-"]:
        input_value = ["-input-"]
        update_multiline_with_timer(window, input_value)
    # if the user closes the window, break the loop
    elif event == sg.WINDOW_CLOSED:
        break

# close the window
window.close ()
