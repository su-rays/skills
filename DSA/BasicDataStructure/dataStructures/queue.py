class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())
print(queue.peek())