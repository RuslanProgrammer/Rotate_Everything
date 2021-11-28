import math
import random
import time
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from PIL import Image, ImageTk

panels = []
counter = None
root = None


def rotate_image(path, index):
    image = Image.open(path)
    # transposed = color_image.transpose(random.choice(range(7)))
    transposed = image.rotate(random.choice(range(361)), expand=True)
    new_path = path.split('.')
    new_path[-2] += '_ROTATED' + str(index)
    transposed.save('.'.join(new_path), format=None)


def show_image(path, index, row, column):
    new_path = path.split('.')
    new_path[-2] += '_ROTATED' + str(index)

    color_image = Image.open('.'.join(new_path))
    img = color_image.resize((50, 50), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(image=img)
    panel = Label(root, image=ph)
    panel.image = ph
    panel.grid(row=row, column=column)
    panels.append(panel)


def click_button():
    for panel in panels:
        panel.grid_forget()
    path = filedialog.askopenfilenames()
    rows = math.ceil(math.sqrt(len(path) * int(counter.get())))

    start_time = time.time()
    for el in path:
        for index in range(int(counter.get())):
            rotate_image(path=el, index=index)
    print(f'{time.time() - start_time} seconds')
    index = 0
    for el in path:
        for count in range(int(counter.get())):
            show_image(el, count, index // rows + 1, index % rows)
            index += 1


def run():
    global root
    root = Tk()
    root.title("Rotate Images FAST!")
    root.geometry("600x300")
    root.resizable(width=True, height=True)

    btn = ttk.Button(root, text="Choose Files", command=click_button)
    btn.grid(row=0, column=0)

    global counter
    counter = StringVar()
    counter_entry = Entry(textvariable=counter)
    counter_entry.grid(row=0, column=2)
    counter.set(100)
    name_label = Label(text="Repeat count:")
    name_label.grid(row=0, column=1)

    root.mainloop()


if __name__ == '__main__':
    run()
