# 1 - We need to implement a python class that represents the queue data structure.
# The class should have these operations:
# - insert(value) => which inserts a new value at the rear of the queue
# - pop() => which returns and removes a value from the front of the queue.
#       We should return None and print a warning message if we tried to pop value from an empty queue
# - is_empty() => which returns True or False to represent whether the queue is empty or not.


class Queue:

    queues = None

    def __init__(self):
        self.queue = []

    def insert(self, value):
        return self.queue.append(value)

    def pop(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)

    @classmethod
    def save(cls):
        pass

    @classmethod
    def load(cls):
        pass

q = Queue()

print(q.is_empty())
q.pop()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert("Ahmed")
q.insert("Hamdi")
print(q.__str__())
q.pop()
q.pop()
print(q.__str__())
print(q.is_empty())