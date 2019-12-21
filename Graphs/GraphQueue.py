class GraphQueue:
    def __init__(self):
        self.current_node = None
        self.counter = 0
        self.head = None

    def enqueue(self, value):
        if self.counter == 0:
            self.head = value
            self.current_node = self.head
            self.counter = self.counter + 1
        else:
            self.current_node.next = value
            self.current_node = self.current_node.next
            self.counter = self.counter + 1

    def dequeue(self):
        return_value = self.head
        self.head = return_value.next
        self.counter = self.counter - 1
        return return_value

    def isEmpty(self):
        if self.counter == 0:
            return True
        else:
            return False
