class Process:

    def __init__(self, color, type):
        self.pid = None
        self.color = color
        self.size = 0
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
        self.segment_list = []
        if type == 'SO':
            s = Segment('S.O.')
            s.size = self.size
            self.segment_list.append(s)
        if type == 'P':
            self.segment_list = [Segment('Code'), Segment('Heap'), Segment('Stack')]


class Segment:
    def __init__(self, name):
        self.name = name
        self.offset = 0
        self.size = 0
        self.base = 0
        self.bound_v_mem = 0
        self.bound_p_mem = 0
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
