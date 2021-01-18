from tkinter import ttk
from tkinter import *
from Process import Process, Block


class Segmentation:

    def __init__(self, window):
        x_init, y_init, x_end, y_end = 0, 0, 300, 450
        self.COLORS = ['royal blue', 'pink', 'blue violet', 'orange', 'white smoke', 'blue', 'bisque2',
                       'cyan', 'saddle brown', 'thistle', 'yellow', 'sandy brown', 'LightYellow4', 'red']
        self.index_color = -1
        self.WIDTH_V_MEM = 70
        self.WIDTH_P_MEM = 300
        self.SIZE_P_MEM = 128
        self.SIZE_SO_MEM = 16
        self.HIGH_P_MEM = 4

        self.address_space = []
        self.free_block_p_mem = []
        for i in range(self.SIZE_P_MEM):
            self.address_space.append(0)

        self.process_list = []
        self.v_mem_x1 = 10
        self.v_mem_y1 = 20
        self.v_mem_x2 = 70
        self.v_mem_y2 = 100

        self.window = window
        self.window.geometry("980x562")
        self.window.resizable(False, False)
        self.window.title("Simulador de Segmentación de Memoria")

        # Memoria Fisica
        self.p_memory = Canvas(self.window, width=300, height=512, bg="green")
        self.p_memory.place(x=655, y=25)

        # Memoria Virtual
        self.v_memory = Canvas(self.window, width=600, height=250, bg="white")
        self.v_memory.place(x=25, y=25)

        # Paint SO in physical memory
        SO = Process('gray60', 'SO', self.SIZE_SO_MEM)
        SO.segment_list[0].size = SO.size
        SO.segment_list[0].x1 = 0
        SO.segment_list[0].y1 = 0
        SO.segment_list[0].x2 = self.WIDTH_P_MEM
        SO.segment_list[0].y2 = SO.size * self.HIGH_P_MEM
        self.paint_in_p_memory(SO)
        self.take_p_memory(0, SO.size)

        # Creating a Frame Container add process
        frame_add_process = LabelFrame(self.window, text='Agregar Proceso')
        frame_add_process.place(x=25, y=300)
        # Virtual Memory Input
        self.label_new_process = Label(frame_add_process, text='Memoria (KB): ').grid(row=1, column=0)
        self.imput_memory_new_process = Entry(frame_add_process)
        self.imput_memory_new_process.focus()
        self.imput_memory_new_process.grid(row=1, column=1)
        # Button Add Process
        ttk.Button(frame_add_process, text='Crear Proceso', command=self.add_process) \
            .grid(row=3, columnspan=2, sticky=W + E)

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
        try:
            memory_new_process = int(self.imput_memory_new_process.get())
            print(memory_new_process)
        except ValueError:
            print("That's not an int!")
            return

        color = self.get_color()
        p = Process(color, 'P', memory_new_process)

        p = self.calculate_in_v_memory(p)
        p = self.calculate_in_p_memory(p)
        self.process_list.append(p)

    def calculate_in_v_memory(self, p):
        p.x1 = self.v_mem_x1
        p.y1 = self.v_mem_y1
        p.x2 = self.v_mem_x2
        p.y2 = self.v_mem_y2
        p.pid_v_mem = self.v_memory.create_rectangle(p.x1, p.y1, p.x2, p.y2, fill=p.color)
        Label(self.v_memory, text='P' + str(p.pid_v_mem), fg='white', bg='black').place(x=p.x1, y=p.y1)
        self.v_mem_x1 += self.WIDTH_V_MEM
        self.v_mem_x2 += self.WIDTH_V_MEM
        return p

    def calculate_in_p_memory(self, p):
        for i in range(len(p.segment_list)):
            block = self.best_fit(p.segment_list[i])
            p.segment_list[i].x2 = self.WIDTH_P_MEM
            p.segment_list[i].y1 = block.start * self.HIGH_P_MEM
            p.segment_list[i].y2 = p.segment_list[i].y1 + (p.segment_list[i].size * self.HIGH_P_MEM)
            self.take_p_memory(block.start, block.start + p.segment_list[i].size)
        self.paint_in_p_memory(p)
        return p

    def get_color(self):
        if self.index_color == (len(self.COLORS) - 1):
            self.index_color = 0
        else:
            self.index_color += 1
        return self.COLORS[self.index_color]

    def paint_in_p_memory(self, p):
        for i in range(len(p.segment_list)):
            p.segment_list[i].pid_p_mem = self.p_memory.create_rectangle(p.segment_list[i].x1, p.segment_list[i].y1,
                                                                         p.segment_list[i].x2, p.segment_list[i].y2,
                                                                         fill=p.color)
            Label(self.p_memory, text=p.segment_list[i].name + ', ' + str(p.segment_list[i].size) + 'KB', fg='white',
                  bg='black') \
                .place(x=p.segment_list[i].x1, y=p.segment_list[i].y1)

    def paint_in_v_memory(self):
        pass

    def best_fit(self, segment):
        self.calculate_free_blocks()
        block_to_return = self.free_block_p_mem[0]
        pass_menor = self.SIZE_P_MEM
        for block in self.free_block_p_mem:
            if segment.size >= block.size and block.size < pass_menor:
                block_to_return = block
        return block_to_return

    def take_p_memory(self, start, end, free=1):
        for i in range(start, end):
            self.address_space[i] = free

    def calculate_free_blocks(self):
        self.free_block_p_mem.clear()
        start_bool = False
        add_block = False
        for i in range(self.SIZE_P_MEM):
            if start_bool:
                if self.address_space[i] == 1:
                    end = i - 1
                    add_block = True
            else:
                if self.address_space[i] == 0:
                    start = i
                    start_bool = True
            if add_block:
                start_bool = False
                add_block = False
                self.free_block_p_mem.append(Block(start, end + 1))
                continue

        if self.address_space[self.SIZE_P_MEM - 1] == 0 and start_bool:
            self.free_block_p_mem.append(Block(start, self.SIZE_P_MEM))

    def del_process(self, id):
        pass
