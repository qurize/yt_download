v = "v.01"
import PySimpleGUI as sg
from pytube import YouTube
import os

sg.theme('DarkTeal9')

layout = [
    [sg.Text('Youtube Audio Download : ')],
    [sg.Text('Save Path', size=(10, 1)), sg.InputText(key='-path-'), sg.Button("Path", size=(5, 1))],
    [sg.Text('URL', size=(10, 1)), sg.InputText(key='-url-')],
    [sg.Button("Download", size=(10, 1)), sg.Exit()]]

window = sg.Window('Simple data entry form', layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["-url-"])
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Path":
        path = sg.popup_get_folder('Please enter a folder name')
        window["-path-"].update(path)

        pass
    if event == 'Download':
        if values["-path-"] != "" and values["-url-"] != "":
            path = values["-path-"]
            print(path.replace("/", "\\"))

            video = YouTube(values["-url-"])
            print("title is : ", video.title)
            video.streams.filter(only_audio=True).first().download(path, filename="TemporaryName.Mp4")

            # remove caracters (" | , / \ ..... ) from video title

            VideoTitle = video.title
            VideoTitle = VideoTitle.replace('\"', " ")
            VideoTitle = VideoTitle.replace('|', " ")
            VideoTitle = VideoTitle.replace(',', " ")
            VideoTitle = VideoTitle.replace('/', " ")
            VideoTitle = VideoTitle.replace('\\', " ")
            VideoTitle = VideoTitle.replace(':', " ")
            VideoTitle = VideoTitle.replace('*', " ")
            VideoTitle = VideoTitle.replace('?', " ")
            VideoTitle = VideoTitle.replace('<', " ")
            VideoTitle = VideoTitle.replace('>', " ")
            VideoTitle = VideoTitle.replace('#', " ")

            # change name and converting Mp4 to Mp3
            my_file = path + "\\" + "TemporaryName.mp4"
            base = path + "\\" + VideoTitle
            print("New Video Title is :" + VideoTitle)
            os.rename(my_file, base + '.mp3')
            window["-url-"].update("")

window.close()
