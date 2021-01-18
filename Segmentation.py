from tkinter import ttk
from tkinter import *
from Process import Process


class Segmentation:

    def __init__(self, window):
        x_init, y_init, x_end, y_end = 0, 0, 300, 450
        self.COLORS = ['yellow', 'blue', 'red', 'royal blue', 'pink', 'blue violet', 'thistle', 'orange', 'white smoke',
                       'bisque2', 'cyan', 'saddle brown', 'sandy brown', 'LightYellow4']
        self.index_color = 0
        self.WIDTH_V_MEM = 70
        self.HIGH_P_MEM = 4

        self.addres_space = []
        for i in range(127):
            self.addres_space.append(0)

        self.process_list = []
        self.v_mem_x1 = 10
        self.v_mem_y1 = 20
        self.v_mem_x2 = 70
        self.v_mem_y2 = 100

        self.window = window
        self.window.geometry("980x562")
        self.window.resizable(False, False)
        self.window.title("Segmentation Simulator")

        # Memoria Fisica
        self.p_memory = Canvas(self.window, width=300, height=512, bg="green")
        self.p_memory.place(x=655, y=25)

        # Paint SO in physical memory
        SO = Process('gray60', 'SO')
        SO.size = 16
        SO.segment_list[0].size = 16
        SO.segment_list[0].x1 = 0
        SO.segment_list[0].y1 = 0
        SO.segment_list[0].x2 = 300
        SO.segment_list[0].y2 = SO.size * self.HIGH_P_MEM
        self.paint_in_p_memory(SO)

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
        p = Process(color, 'P')

        p = self.calculate_in_v_memory(p)
        # p = self.calculate_in_p_memory(p)
        self.process_list.append(p)

    def calculate_in_v_memory(self, p):
        p.x1 = self.v_mem_x1
        p.y1 = self.v_mem_y1
        p.x2 = self.v_mem_x2
        p.y2 = self.v_mem_y2
        p.pid = self.v_memory.create_rectangle(p.x1, p.y1, p.x2, p.y2, fill=p.color)
        Label(self.v_memory, text='P' + str(p.pid), fg='white', bg='black').place(x=p.x1, y=p.y1)
        self.v_mem_x1 += self.WIDTH_V_MEM
        self.v_mem_x2 += self.WIDTH_V_MEM
        return p

    def calculate_in_p_memory(self, p):
        if p.x1 is None:
            # best_fit()
            x1, y1, x2, y2 = 0, 64, 300, 180

        self.r2 = self.p_memory.create_rectangle(p.x1, p.y1, p.x2, p.y2, fill=p.color)

    def del_process(self, id):
        pass

    def get_color(self):
        if self.index_color == (len(self.COLORS) - 1):
            self.index_color = 0
        else:
            self.index_color += 1
        return self.COLORS[self.index_color]

    def paint_in_p_memory(self, p):
        for segment in p.segment_list:
            self.r2 = self.p_memory.create_rectangle(segment.x1, segment.y1, segment.x2, segment.y2, fill=p.color)
            Label(self.p_memory, text=segment.name + ' - ' + str(segment.size) + 'KB', fg='white', bg='black')\
                .place(x=segment.x1, y=segment.y1)

    def paint_in_v_memory(self):
        pass

    def best_fit(self):
        pass
