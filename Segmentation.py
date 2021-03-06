from tkinter import ttk
from tkinter import *
from Process import Process, Block


class Segmentation:

    def __init__(self, window):
        x_init, y_init, x_end, y_end = 0, 0, 300, 450
        self.COLORS = ['royal blue', 'blue violet', 'orange', 'blue',
                       'cyan', 'saddle brown', 'thistle', 'yellow', 'sandy brown', 'LightYellow4', 'red']
        self.SIZE_P_MEM = 128
        self.SIZE_SO_MEM = 16
        self.WIDTH_V_MEM = 70
        self.WIDTH_P_MEM = 300
        self.HIGH_P_MEM = 4
        self.index_color = -1
        self.free_block_p_mem = []
        self.process_list = []
        self.free_memory = True
        self.address_space = list(range(self.SIZE_P_MEM))
        self.take_p_memory(0, self.SIZE_P_MEM, 0)
        self.v_mem_x1 = 10
        self.v_mem_y1 = 20
        self.v_mem_x2 = 70
        self.v_mem_y2 = 100

        self.window = window
        self.window.geometry("980x562")
        self.window.resizable(False, False)
        self.window.title("Simulador de Segmentación de Memoria")

        # Memoria Fisica
        self.paint_canvas_p_virtual()

        # Memoria Virtual
        self.paint_canvas_v_virtual()

        # Creating a Frame Container add process
        frame_add_process = LabelFrame(self.window, text='Agregar Proceso')
        frame_add_process.place(x=25, y=300)

        self.show_message()
        self.show_message("Para crear un nuevo proceso, especifique el tamaño en KB y presione 'Crear Proceso'")

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
        self.input_id_del_process = Entry(frame_del_process)
        self.input_id_del_process.grid(row=1, column=1)
        # Button Add Product
        ttk.Button(frame_del_process, text='Terminar Proceso', command=self.del_process).grid(row=3, columnspan=2,
                                                                                              sticky=W + E)

    def add_process(self):
        try:
            memory_new_process = int(self.imput_memory_new_process.get())
        except ValueError:
            self.show_message('No es un numero valido')
            return
        self.imput_memory_new_process.delete(0, 'end')
        self.free_memory = True
        color = self.get_color()
        p = Process(color, 'P', memory_new_process)

        p = self.calculate_in_p_memory(p)
        if self.free_memory:
            p = self.calculate_in_v_memory(p)
            self.show_message("Proceso creado correctamente con Pid={}.".format(p.pid_v_mem))
            self.process_list.append(p)
            self.show_register_values(p)
        else:
            return

    def calculate_in_v_memory(self, p):
        p.x1 = self.v_mem_x1
        p.y1 = self.v_mem_y1
        p.x2 = self.v_mem_x2
        p.y2 = self.v_mem_y2
        p.pid_v_mem = self.v_memory.create_rectangle(p.x1, p.y1, p.x2, p.y2, fill=p.color)
        Label(self.v_memory, text='P-' + str(p.pid_v_mem) + ', ' + str(p.size) + 'KB', fg='white', bg='black') \
            .place(x=p.x1, y=p.y1)
        self.v_mem_x1 += self.WIDTH_V_MEM
        self.v_mem_x2 += self.WIDTH_V_MEM
        return p

    def calculate_in_p_memory(self, p):
        for i in range(len(p.segment_list)):
            block = self.best_fit(p.segment_list[i])
            if block is None:
                self.show_message("No hay memoria suficiente para crear el proceso")
                self.free_memory = False
                return
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
                  bg='black').place(x=p.segment_list[i].x1, y=p.segment_list[i].y1)

    def best_fit(self, segment):
        self.calculate_free_blocks()
        block_to_return = Block(0, 0)
        pass_menor = self.SIZE_P_MEM
        for block in self.free_block_p_mem:
            if block.size >= segment.size and block.size < pass_menor:
                block_to_return = block
                pass_menor = block.size
        if block_to_return.size < segment.size:
            return None
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

    def paint_canvas_v_virtual(self):
        self.v_memory = Canvas(self.window, width=600, height=250, bg="white")
        self.v_memory.place(x=25, y=25)
        Label(self.window, text='Memorias Vituales: ').place(x=290, y=5)

    def paint_canvas_p_virtual(self):
        self.p_memory = Canvas(self.window, width=300, height=512, bg="green")
        self.p_memory.place(x=655, y=25)
        Label(self.window, text='Memoria Física: ').place(x=760, y=5)

        # Paint SO in physical memory
        SO = Process('gray60', 'SO', self.SIZE_SO_MEM)
        SO.segment_list[0].size = SO.size
        SO.segment_list[0].x1 = 0
        SO.segment_list[0].y1 = 0
        SO.segment_list[0].x2 = self.WIDTH_P_MEM
        SO.segment_list[0].y2 = SO.size * self.HIGH_P_MEM
        self.paint_in_p_memory(SO)
        self.take_p_memory(0, SO.size)

    def del_process(self):
        try:
            id_del_process = int(self.input_id_del_process.get())
        except ValueError:
            self.show_message('No es un numero valido')
            return

        self.input_id_del_process.delete(0, 'end')
        index_v_mem = -1
        index_p_mem = []
        index_list = -1
        for i in range(len(self.process_list)):
            if id_del_process == self.process_list[i].pid_v_mem:
                index_v_mem = self.process_list[i].pid_v_mem
                index_list = i
                for segment in self.process_list[i].segment_list:
                    index_p_mem.append(segment)
                continue
        if index_list == -1:
            self.show_message("El proceso con Pid = {} no existe.".format(id_del_process))
            return

        del self.process_list[index_list:index_list + 1]
        self.del_process_v_memory(index_v_mem)
        self.del_process_p_memory(index_p_mem)
        self.input_id_del_process['text'] = ''
        self.show_message("El proceso con Pid = {} ha sido borrado.".format(id_del_process))

    def del_process_v_memory(self, index):
        self.v_memory.delete(index)

    def del_process_p_memory(self, segments):
        self.paint_canvas_p_virtual()
        for segment in segments:
            self.take_p_memory(segment.y1 // self.HIGH_P_MEM, segment.y2 // self.HIGH_P_MEM, 0)
        self.paint_all_p_memory()

    def paint_all_p_memory(self):
        for process in self.process_list:
            self.paint_in_p_memory(process)

    def show_message(self, message=''):
        if message == '':
            frame_message = LabelFrame(self.window, text='Mensajes')
            frame_message.place(x=25, y=500)
            self.message = Label(frame_message, text="", font="20")  # fg='red'
            self.message.grid(row=0, column=0, columnspan=2, sticky=W + E)
        else:
            self.message['text'] = message

    def show_register_values(self, p):
        register_values = "Segment Register Values\n"
        register_values += f"Pid = {p.pid_v_mem}\n"
        register_values += "----------------------\n"
        register_values += f"Segment\tBase\tSize\tGP\n"
        for i, segment in enumerate(p.segment_list):
            register_values += f"{segment.name}\t{segment.y1 // self.HIGH_P_MEM}\t{segment.size}\t{1 if i < 2 else 0}\n"

        Label(self.window, text=register_values, font="20", bg=p.color, fg='black').place(x=250, y=167)
