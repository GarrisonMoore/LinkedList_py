

class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def append_before(self):
        pass

    def append_after(self):
        pass

    def pop_before(self):
        pass

    def pop_after(self):
        pass

    def return_data(self):
        pass

    def next(self):
        pass


class LinkedList:
    def __init__(self,nodes=None):
        self.head = None