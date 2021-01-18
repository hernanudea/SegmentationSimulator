class Process:

    def __init__(self, color, type_process, size):
        self.NUMBER_BLOCK = 3
        self.pid_v_mem = None
        self.color = color
        self.size = size
        self.segment_list = []
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
        if type_process == 'SO':
            so = Segment('S.O.', self.size)
            self.segment_list.append(so)
        if type_process == 'P':
            code = Segment('Code', self.size // self.NUMBER_BLOCK)
            heap = Segment('Heap', self.size // self.NUMBER_BLOCK)
            stack = Segment('Stack', self.size - (code.size + heap.size))
            self.segment_list.append(code)
            self.segment_list.append(heap)
            self.segment_list.append(stack)


class Segment:
    def __init__(self, name, size):
        self.pid_p_mem = None
        self.name = name
        self.size = size
        self.offset = 0
        self.base = 0
        self.bound_v_mem = 0
        self.bound_p_mem = 0
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0


class Block:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.size = self.end - self.start
