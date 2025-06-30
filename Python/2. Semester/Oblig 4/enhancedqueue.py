from collections import deque

class EnhancedDeque(deque):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def append_left_if_not_exists(self, data):
        new_node = EnhancedDeque(data)
        if new_node not in self.data:
            new_node.append()