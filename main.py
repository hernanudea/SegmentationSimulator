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

        # Creating a Frame Container add process
        frame_add_process = LabelFrame(self.window, text='Agregar Proceso')
        frame_add_process.place(x=25, y=300)
        # Name Input
        Label(frame_add_process, text='Memoria (KB): ').grid(row=1, column=0)
        self.memory_new_process = Entry(frame_add_process)
        self.memory_new_process.focus()
        self.memory_new_process.grid(row=1, column=1)
        # Button Add Product
        ttk.Button(frame_add_process, text='Crear Proceso', command=self.add_process).grid(row=3, columnspan=2, sticky=W + E)

        # Creating a Frame Container delete process
        frame_del_process = LabelFrame(self.window, text='Terminar Proceso')
        frame_del_process.place(x=300, y=300)
        # Name Input
        Label(frame_del_process, text='Id proceso: ').grid(row=1, column=0)
        self.memory_del_process = Entry(frame_del_process)
        self.memory_del_process.grid(row=1, column=1)
        # Button Add Product
        ttk.Button(frame_del_process, text='Terminar Proceso', command=self.del_process).grid(row=3, columnspan=2, sticky=W + E)


    def add_process(self):
        # redimensionar
        # x0, y0, x1, y1 = self.canvas.coords(self.sss)
        # y1 /= 2
        # self.canvas.coords(self.sss, x0, y0, x1, y1)
        self.r2 = self.p_memory.create_rectangle(0, 50, 300, 180, fill='yellow')
        self.r3 = self.p_memory.create_rectangle(0, 190, 300, 270, fill='blue')
        self.r4 = self.p_memory.create_rectangle(0, 275, 300, 350, fill='red')

        self.r4 = self.v_memory.create_rectangle(10, 10, 70, 100, fill='yellow')
        self.r4 = self.v_memory.create_rectangle(80, 10, 140, 100, fill='blue')
        self.r4 = self.v_memory.create_rectangle(150, 10, 210, 100, fill='red')
        self.r4 = self.v_memory.create_rectangle(220, 10, 280, 100, fill='royal blue')
        self.r4 = self.v_memory.create_rectangle(290, 10, 350, 100, fill='pale green')
        self.r4 = self.v_memory.create_rectangle(360, 10, 420, 100, fill='blue violet')
        self.r4 = self.v_memory.create_rectangle(430, 10, 490, 100, fill='thistle')
        self.r4 = self.v_memory.create_rectangle(500, 10, 560, 100, fill='orange')
        self.r4 = self.v_memory.create_rectangle(640, 10, 700, 100, fill='blue')

    def del_process(self, id):
        pass


if __name__ == '__main__':
    window = Tk()
    app = Segmentation(window)
    window.mainloop()
