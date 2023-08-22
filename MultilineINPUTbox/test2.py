import PySimpleGUI as sg
import time

def my_long_operation():
    time.sleep(1)

    return "sleep now"


def main():
    layout =[
     [sg.Text('My Window')],
                [sg.Input(key='-IN-')],
                [sg.Text(key='-OUT-')],
                [sg.Button('Go'), sg.Button('Threaded'), sg.Button('Dummy')  ]

    ]

    window = sg.Window('Window Title', layout, keep_on_top=True)  
    while True:
        event, values = window.read()  
        if event == sg.WIN_CLOSED:
            break

        window['-OUT-'].update(f'{event, values}')
        window.refresh()

        if event == 'GO':
            return_value = my_long_operation()
            window['-OUT-'].Update(f'direct return value ={return_value}')
        elif event == 'Threaded':
            # Let PySimpleGUI do the threading for you...
            window.perform_long_operation(my_long_operation, '-OPERATION DONE-')
        elif event == '-OPERATION DONE-':    
            window['-OUT-'].Update(f'indirect return value = {values[event]}') 
    window.close()

if __name__ == '__main__':
    main()



