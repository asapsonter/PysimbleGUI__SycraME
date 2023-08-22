import PySimpleGUI as sg
import threading
import json
from enum import Enum
# Define an enum class for the keys
class AllEvt(Enum):
    gpMultilineKey = '-MLINE-'
    gpInputTextKey = '-INPUT-'
    gpAddBtntest = '-ADD-'

# Define a class for the global variables
class AppGlobal:
    def __init__(self):
        self.gpMultilineKey = AllEvt.gpMultilineKey.value
        self.gpInputTextKey = AllEvt.gpInputTextKey.value
        self.gpAddBtntest = AllEvt.gpAddBtntest.value

# Define a function to make the layout
def make_grouping_layout(globalVar: AppGlobal):
    #declare layout object
    layout = [
        #[sg.Column(right_column_layout, element_justification='center', size=(600, None)) ]
        [sg.Text('\n             Group Added \n', font=(15), text_color='black', justification='center')],
        
        [sg.Text('List of scanned devices:', font=( 12), text_color='black', justification='left')],
         #multiline input
        [ sg.Multiline(key=globalVar.gpMultilineKey, enable_events=True, autoscroll=True, size=(60,4),
                    background_color='#999999',  disabled=True )],    
        [sg.InputText(key=globalVar.gpInputTextKey, enable_events=True, size=(60, 1))],
        [sg.Button('\n Add \n', key=globalVar.gpAddBtntest, button_color=('#000000', '#b6eada'), size=(8, 1))]
    ]
    return layout

# Define a function to append an input value to the Multiline element and clear the input field
def append_input(window, input_value):
    # Write a custom event and value to the window
    window.write_event_value("-APPEND-", input_value)

# Define a function to store the Multiline element value in a JSON format
def store_json(window):
    # Get the Multiline element value
    multiline_value = window[AllEvt.gpMultilineKey.value].get()
    # Split the value by newline characters
    multiline_list = multiline_value.split("\n")
    # Remove any empty strings from the list
    multiline_list = list(filter(None, multiline_list))
    # Convert the list to a JSON string
    json_string = json.dumps(multiline_list)
    # Write a custom event and value to the window
    window.write_event_value("-STORE-", json_string)

# Define a function to handle the events
def handle_events(window):
    # Create a variable to store the timer object
    timer = None

    # Event loop
    while True:
        event, values = window.read()
        # If user closes window or clicks Exit, break the loop
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        # If user types something in the Input element, create a timer to append it to the Multiline element after 1 second
        elif event == AllEvt.gpInputTextKey.value:
            # Cancel the previous timer if it exists
            if timer is not None:
                timer.cancel()
            # Get the input value
            input_value = values[event]
            # Create a new timer that will call a function after 1 second
            timer = threading.Timer(1.0, append_input, args=(window, input_value))
            # Start the timer
            timer.start()
        # If a custom event is received from the timer, append the input value to the Multiline element and clear the input field
        elif event == "-APPEND-":
            # Get the input value from the event value
            input_value = values[event]
            # Append the input value to the Multiline element
            window[AllEvt.gpMultilineKey.value].update(input_value + "\n", append=True)
            # Clear the input field
            window[AllEvt.gpInputTextKey.value].update("")
        # If user clicks on the Add button, store the Multiline element value in a JSON format and print it out
        elif event == AllEvt.gpAddBtntest.value:
            # Call a function to store the Multiline element value in a JSON format
            store_json(window)
        # If a custom event is received from the store_json function, print out the JSON string
        elif event == "-STORE-":
            # Get the JSON string from the event value
            json_string = values[event]
            # Print out the JSON string
            print(json_string)

# Define a main function that creates the window and calls the handle_events function
def main():
    # Create an instance of the global variables class
    globalVar = AppGlobal()

    # Create a window with the layout
    window = sg.Window("Grouping Example", make_grouping_layout(globalVar))

    # Call the function to handle the events
    handle_events(window)

    # Close the window
    window.close()

# Call the main function if this file is run as a script
if __name__ == "__main__":
    main()