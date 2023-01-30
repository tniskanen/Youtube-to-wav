import PySimpleGUI as sg
from mp4 import get_mp4


#sg.theme()

layout = [[sg.Text('URL:')],
          [sg.InputText(key='url')],
          [sg.Text('Save Location:')],
          [sg.InputText(key='location'), sg.FolderBrowse()],
          [sg.Radio('MP4', 'b1', default=True, key='mp4'), sg.Radio('WEBM', 'b1')],
          [sg.B('Convert')]]

window = sg.Window('Youtube to MP4 Converter', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Convert':
        if values['mp4'] == True:
            type = 140
        else:
            type = 251
        spot = rf'{values["location"]}'
        get_mp4(values['url'], spot, type)
