from tkinter import ttk
from tkinter import *


class Segmentation:

    def __init__(self, window):
        x_init, y_init, x_end, y_end = 0, 0, 300, 450
        self.window = window
        self.window.geometry("980x500")
        self.window.resizable(False, False)
        self.window.title("Segmentation Simulator")

        # Memoria Fisica
        self.p_memory = Canvas(self.window, width=300, height=450, bg="green")
        self.p_memory.place(x=655, y=25)

        # Memoria Virtual
        self.v_memory = Canvas(self.window, width=600, height=250)
        self.v_memory.place(x=25, y=25)

        ttk.Button(self.window, text='New Process', command=self.add_process).place(x=3, y=2)

    def add_process(self):
        # redimensionar
        # x0, y0, x1, y1 = self.canvas.coords(self.sss)
        # y1 /= 2
        # self.canvas.coords(self.sss, x0, y0, x1, y1)
        self.r2 = self.p_memory.create_rectangle(0, 50, 300, 180, fill='yellow')
        self.r3 = self.p_memory.create_rectangle(0, 190, 300, 270, fill='blue')
        self.r4 = self.p_memory.create_rectangle(0, 275, 300, 350, fill='pink')

        self.r4 = self.v_memory.create_rectangle(10, 10, 70, 100, fill='pink')
        self.r4 = self.v_memory.create_rectangle(80, 10, 140, 100, fill='pink')
        self.r4 = self.v_memory.create_rectangle(150, 10, 210, 100, fill='pink')
        self.r4 = self.v_memory.create_rectangle(220, 10, 280, 100, fill='pink')
        self.r4 = self.v_memory.create_rectangle(290, 10, 350, 100, fill='pink')
        self.r4 = self.v_memory.create_rectangle(360, 10, 420, 100, fill='pink')
        self.r4 = self.v_memory.create_rectangle(430, 10, 490, 100, fill='pink')
        self.r4 = self.v_memory.create_rectangle(500, 10, 560, 100, fill='yellow')
        self.r4 = self.v_memory.create_rectangle(570, 10, 630, 100, fill='red')
        self.r4 = self.v_memory.create_rectangle(640, 10, 700, 100, fill='blue')


if __name__ == '__main__':
    window = Tk()
    app = Segmentation(window)
    window.mainloop()
