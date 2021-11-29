import random
from tkinter import Label

from PIL import Image, ImageTk


def rotate_image(path, index, angle):
    image = Image.open(path)
    transposed = image.rotate(angle)
    if angle == 0:
        transposed = image.rotate(random.choice(range(361)), expand=True)
    new_path = path.split('.')
    new_path[-2] += '_ROTATED' + str(index)
    transposed.save('.'.join(new_path))


def show_image(path, index, row, column, panels, root):
    new_path = path.split('.')
    new_path[-2] += '_ROTATED' + str(index)

    color_image = Image.open('.'.join(new_path))
    img = color_image.resize((50, 50), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(image=img)
    panel = Label(root, image=ph)
    panel.image = ph
    panel.grid(row=row, column=column)
    panels.append(panel)
