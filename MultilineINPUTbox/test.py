import PySimpleGUI as sg
import threading

# Define a function to append an input value to the Multiline element and clear the input field
def append_input(window, input_value):
    # Append the input value to the Multiline element
    window["-MLINE-"].update(input_value + "\n", append=True)
    # Clear the input field
    window["-INPUT-"].update("")

# Create a layout with a Multiline element and an Input element
layout = [
    [sg.Multiline(size=(60, 10), key="-MLINE-", disabled=True)],
    [sg.InputText(key="-INPUT-", enable_events=True, size=(60, 10))] # Add enable_events=True here
]

# Create a window with the layout
window = sg.Window("Multiline Example", layout)

# Create a variable to store the timer object
timer = None

# Event loop
while True:
    event, values = window.read()
    # If user closes window or clicks Exit, break the loop
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    # If user types something in the Input element, create a timer to append it to the Multiline element after 3 seconds
    elif event == "-INPUT-":
        # Cancel the previous timer if it exists
        if timer is not None:
            timer.cancel()
        # Get the input value
        input_value = values["-INPUT-"]
        # Create a new timer that will call a function after 0.5 seconds
        timer = threading.Timer(0.5, append_input, args=(window, input_value))
        # Start the timer
        timer.start()
    

# Close the window
window.close()
