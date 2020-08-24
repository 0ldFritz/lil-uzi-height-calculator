import PySimpleGUI as sg

sg.theme('tealmono')  # please make your windows colorful

layout = [[sg.Text('enter your height'), sg.Input(default_text='feet', key='-feet-'), sg.Input(default_text='inches', key='-inches-')],
          [sg.Text('enter how much money you have (with no comma) '), sg.Input(key='-money-')],
          [sg.Button('Show'), sg.Button('Exit')]]


window = sg.Window('Lil vert unit calculator', layout)

while True:  # Event Loop
    event, values = window.read()
    
    height = (int(values['-feet-']) * 12) + int(values['-inches-'])
    money_height = ((int(values['-money-']) / 100) * 0.0043)
    
    print(event, values)
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        window.FindElement('-feet-').Update('')
        window.FindElement('-inches-').Update('')
        window.FindElement('-money-').Update('')
        sg.popup((height + money_height) / 12)

window.close()