import math
import time
from multiprocessing import Process
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from utils import rotate_image, show_image

panels = []
counter = None
angle = None
root = None


def click_button():
    for panel in panels:
        panel.grid_forget()
    path = filedialog.askopenfilenames()
    rows = math.ceil(math.sqrt(len(path) * int(counter.get())))

    start_time = time.time()

    futures = []
    for el in path:
        for index in range(int(counter.get())):
            process = Process(target=rotate_image, args=(el, index, int(angle.get())))
            process.start()
            futures.append(process)

    for process in futures:
        process.join()
    print(f'{time.time() - start_time} seconds')

    index = 0
    for el in path:
        for count in range(int(counter.get())):
            show_image(el, count, index // rows + 1, index % rows, panels, root)
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

    global angle
    angle = StringVar()
    angle_entry = Entry(textvariable=angle)
    angle_entry.grid(row=0, column=4)
    angle.set(0)
    angle_label = Label(text="Angle (left 0 for random):")
    angle_label.grid(row=0, column=3)
    root.mainloop()

    root.mainloop()


if __name__ == '__main__':
    run()
