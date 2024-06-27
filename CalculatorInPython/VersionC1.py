import PySimpleGUI as sg

# Initialize the GUI window
layout = [[sg.Text('', key='-TEXT-')],
          [sg.Button('0'), sg.Button('1'), sg.Button('2')],
          [sg.Button('3'), sg.Button('4'), sg.Button('5')],
          [sg.Button('6'), sg.Button('7'), sg.Button('8')],
          [sg.Button('9'), sg.Button('.')]]

window = sg.Window('Calculator', layout)

current_num = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)

window.close()
