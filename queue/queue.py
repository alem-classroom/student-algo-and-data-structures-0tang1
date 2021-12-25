class Queue:
    def __init__(self):
        # initialize Queue such that there is a list called 'values' where you store elements
        # 'front' which is the index of the element that is on the front of the queue
        # 'back' which is the index of the element that is on the back of the queue
        values = []

    def enqueue(self, value):
        # add value to the queue
        values.append(value)

    def get_front(self):
        # return value that is first in the queue
        return values[0]

    def dequeue(self):
        # remove first element of the queue and return it
        # if queue is empty, return "Queue is empty"
        if len(values) == 0:
            return "Queue is empty"
        else:
            values.pop(0)

    def get_size(self):
        # return size of the queue
        return len(values)
    
    def clear(self):
        # clear the queue
        values.clear()