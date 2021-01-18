from tkinter import ttk
from tkinter import *
from Process import Process, Segment


class Segmentation:

    def __init__(self, window):
        x_init, y_init, x_end, y_end = 0, 0, 300, 450
        self.COLORS = ['yellow', 'blue', 'red', 'royal blue', 'pink', 'blue violet', 'thistle', 'orange', 'white smoke',
                       'bisque2', 'cyan', 'saddle brown', 'sandy brown', 'LightYellow4']
        self.index_color = 0

        self.process_in_v_mem = []
        self.v_mem_x1 = 10
        self.v_mem_y1 = 20
        self.v_mem_x2 = 70
        self.v_mem_y2 = 100

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
        # Virtual Memory Input
        self.label_new_process = Label(frame_add_process, text='Memoria (KB): ').grid(row=1, column=0)
        self.memory_new_process = Entry(frame_add_process)
        self.memory_new_process.focus()
        self.memory_new_process.grid(row=1, column=1)
        # Button Add Process
        ttk.Button(frame_add_process, text='Crear Proceso', command=self.add_process).grid(row=3, columnspan=2,
                                                                                           sticky=W + E)

        # Creating a Frame Container delete process
        frame_del_process = LabelFrame(self.window, text='Terminar Proceso')
        frame_del_process.place(x=300, y=300)
        # Name Input
        Label(frame_del_process, text='Id proceso: ').grid(row=1, column=0)
        self.memory_del_process = Entry(frame_del_process)
        self.memory_del_process.grid(row=1, column=1)
        # Button Add Product
        ttk.Button(frame_del_process, text='Terminar Proceso', command=self.del_process).grid(row=3, columnspan=2,
                                                                                              sticky=W + E)

    def add_process(self):
        # try:
        #     memory_new_process = int(self.label_new_process.get())
        #     print(memory_new_process)
        # except ValueError:
        #     print("That's not an int!")
        #
        #     return

        # redimensionar
        # x0, y0, x1, y1 = self.canvas.coords(self.sss)
        # y1 /= 2
        # self.canvas.coords(self.sss, x0, y0, x1, y1)
        color = self.get_color()
        self.paint_in_p_memory(color)

        self.paint_in_v_memory(color)

    def del_process(self, id):
        pass

    def get_color(self):
        if self.index_color == (len(self.COLORS) - 1):
            self.index_color = 0
        else:
            self.index_color += 1
        return self.COLORS[self.index_color]

    def paint_in_p_memory(self, color):
        # best_fit()
        self.r2 = self.p_memory.create_rectangle(0, 50, 300, 180, fill=color)
        self.r3 = self.p_memory.create_rectangle(0, 190, 300, 270, fill='blue')
        self.r4 = self.p_memory.create_rectangle(0, 275, 300, 350, fill='red')

    def paint_in_v_memory(self, color):
        pid = self.v_memory.create_rectangle(self.v_mem_x1, self.v_mem_y1, self.v_mem_x2, self.v_mem_y2, fill=color)
        self.process_in_v_mem.append(pid)
        Label(self.v_memory, text='P' + str(len(self.process_in_v_mem)), fg='white', bg='black')\
            .place(x=self.v_mem_x1, y=self.v_mem_y1)
        self.v_mem_x1 += 70
        self.v_mem_x2 += 70

    def best_fit(self):
        pass