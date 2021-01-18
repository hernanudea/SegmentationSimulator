class Process:

    def __init__(self, pid):
        self.pid = pid
        self.color = ''
        self.segment_list = [Segment('Code'), Segment('Heap'), Segment('Stack')]


class Segment:
    def __init__(self, name):
        self.name = name
        self.offset = 0
        self.size =0
        self.base = 0
        self.bound_v_mem = 0
        self.bound_p_mem = 0
