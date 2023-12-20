from PIL import Image
from typing import List

import PySimpleGUI as gui
from actions import mirror, grey, invert

def get_raw_image(name: str) -> List[List[List[int]]]:
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []

    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i * num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data


def image_from_raw(raw: List[List[List[int]]], name: str) -> None:
    image = Image.new("RGB", (len(raw[0]), len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)



layout = [[gui.Text("")], [gui.Button("OK")]]

# Create the window
window = gui.Window("Demo", layout)
gui.Window(title="Simple Image Editor", layout=[[]], margins=(400, 400)).read()

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == gui.WIN_CLOSED:
        break

window.close()