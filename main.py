from PIL import Image, ImageTk
from typing import List
from io import BytesIO

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

def resize_image(image_path, max_size=(400, 400)):
    """Resize the image to fit within max_size."""
    img = Image.open(image_path)
    img.thumbnail(max_size)
    with BytesIO() as byte_io:
        img.save(byte_io, format="PNG")
        return byte_io.getvalue()
def pickfilemenu () -> str:
    uploadlayout = [
        [gui.Text("Select an image file (JPG or PNG):")],
        [gui.Input(key="-FILE-", enable_events=True, visible=False),
         gui.FileBrowse(button_text="Browse", file_types=(("Image Files", "*.jpg;*.png"),))],
        [gui.Button("Submit"), gui.Button("Exit")]
    ]
    #layout = [[gui.Text("")], [gui.Button("OK")]]
    # Create the window
    window = gui.Window("Demo", uploadlayout)
    # gui.Window(title="Simple Image Editor", layout=[[]], margins=(400, 400)).read()
    file_path = ''
    while True:
        event, values = window.read()

        if event == "Submit":
            file_path = values["-FILE-"]
            if file_path:
                gui.popup(f"File selected: {file_path}")
                event = "Exit"

            else:
                gui.popup_error("No file selected! Please choose a file.")
        # End program if user closes window or
        # presses the OK button
        if event == "Exit" or event == gui.WIN_CLOSED:
            break

    window.close()
    return file_path
def editor (filename: str):
    layout = [
        [gui.Text ("Python Image Editor")],
        [gui.Image(key="-IMAGE-", size=(400, 400))],
        [gui.VPush()],
        [gui.Button ("Mirror"), gui.Button("Grey"), gui.Button ("Invert"), gui.Button ("Revert to Original")]
        ]

    CONST_DEFAULT = filename
    window = gui.Window ("Python Image Editor" , layout, size = (500,500))

    while True:
        event, values = window.read()
        check_if_edited = False



        #mirror button function
        if event == "Mirror":
            try:
                # Update the image element with the selected file
                image_pixel_list = get_raw_image(filename)
                newrgb = mirror(image_pixel_list)

                if check_if_edited == False:
                    filename = "new_edited_image.png"
                    check_if_edited = True

                image_from_raw(newrgb, "new_edited_image.png")
                image_data = resize_image(filename, max_size=(400, 400))


                window["-IMAGE-"].update(data = image_data)
            except Exception as e:
                gui.popup_error(f"Error displaying image: {e}")

        #grey
        if event == "Grey":
            try:
                # Update the image element with the selected file
                image_pixel_list = get_raw_image(filename )
                newrgb = grey(image_pixel_list)

                if check_if_edited == False:
                    filename = "new_edited_image.png"
                    check_if_edited = True

                image_from_raw(newrgb, "new_edited_image.png")

                image_data = resize_image(filename, max_size=(400, 400))
                window["-IMAGE-"].update(data = image_data)
            except Exception as e:
                gui.popup_error(f"Error displaying image: {e}")

        #invert
        if event == "Invert":
            try:
                # Update the image element with the selected file

                image_pixel_list = get_raw_image(filename)


                newrgb = invert(image_pixel_list)

                #makes sure that the image fits inside the container


                if check_if_edited == False:
                    filename = "new_edited_image.png"
                    check_if_edited = True
                image_from_raw(newrgb, "new_edited_image.png")
                image_data = resize_image(filename, max_size=(400, 400))
                window["-IMAGE-"].update(data = image_data)
            except Exception as e:
                gui.popup_error(f"Error displaying image: {e}")


        #revert
        if event == "Revert to Original":
            try:
                # Update the image element with the selected file
                image_pixel_list = get_raw_image(CONST_DEFAULT)

                image_from_raw(image_pixel_list, "new_edited_image.png")
                image_data = resize_image("new_edited_image.png", max_size=(400, 400))
                window["-IMAGE-"].update(data = image_data)

            except Exception as e:
                gui.popup_error(f"Error displaying image: {e}")



        if event == "Exit" or event == gui.WIN_CLOSED:
            break

    window.close()

 ##########################
def mainmenu ():


    uploadlayout = [
        [gui.Text("Python Image Editor")],
        [gui.VPush()],
        [ gui.Button("Upload own image"), gui.Button ("Use Default Image"), gui.Button("Exit")]
    ]
    layout = [[gui.Text("")], [gui.Button("OK")]]

    # Create the window
    window = gui.Window("Demo", uploadlayout, size = (600, 600))
    # gui.Window(title="Simple Image Editor", layout=[[]], margins=(400, 400)).read()
    CONST_DEFAULTIMAGE = get_raw_image("Defaultimage.png")
    selectedImage = CONST_DEFAULTIMAGE
    while True:
        event, values = window.read()
        if event == "Upload own image":
            file = pickfilemenu()
            if file != '':
                selectedImage = file
                editor(selectedImage)
        if event == "Use Default Image":
            selectedImage = CONST_DEFAULTIMAGE
            editor("Defaultimage.png")



        if event == "Exit" or event == gui.WIN_CLOSED:
            break

    window.close()

#nested_rgb_image_list = get_raw_image("Defaultimage.png")
#mirror (nested_rgb_image_list)
#image_from_raw(nested_rgb_image_list, "new_edited_image.png")

mainmenu()


