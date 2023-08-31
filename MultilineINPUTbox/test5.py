import PySimpleGUI as sg
import threading
import json
from enum import Enum
class AllEvt(Enum):
    gpMultilineKey = '-MLINE-'
    gpInputTextKey = '-INPUT-'
    gpAddBtntest = '-ADD-'

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

def append_input(window, input_value):
    window.write_event_value("-APPEND-", input_value)
def store_json(window):
    multiline_value = window[AllEvt.gpMultilineKey.value].get()
    multiline_list = multiline_value.split("\n")
    multiline_list = list(filter(None, multiline_list))
    json_string = json.dumps(multiline_list)
    window.write_event_value("-STORE-", json_string)

def handle_events(window):
    timer = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == AllEvt.gpInputTextKey.value:
            if timer is not None:
                timer.cancel()
            input_value = values[event]
            timer = threading.Timer(1.0, append_input, args=(window, input_value))
            timer.start()
        elif event == "-APPEND-":
            input_value = values[event]
            window[AllEvt.gpMultilineKey.value].update(input_value + "\n", append=True)
            window[AllEvt.gpInputTextKey.value].update("")
        elif event == AllEvt.gpAddBtntest.value:
            store_json(window)
        elif event == "-STORE-":
            json_string = values[event]
            print(json_string)

def main():
    globalVar = AppGlobal()

    window = sg.Window("Grouping Example", make_grouping_layout(globalVar))

    handle_events(window)

    window.close()

if __name__ == "__main__":
    main()