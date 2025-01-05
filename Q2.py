import queue_Q1

# 2 - We need to implement another queue class that has the same properties as previous but with the following changes:
# A. The queue should have a name that is provided as a parameter of its constructor
# B. The queue should have a size that is provided as a parameter of its constructor and if we tried to insert more values than its size raises a
# custom exception called QueueOutOfRangeException
# C. The queue keeps track with all queues instances that has been created through this class and we can get any queue of them using its name
# D. The queue class should have two class methods called (save, load)
# which saves all created queues instances to a file and load them when needed. (bonus)

class Queue2(queue_Q1.Queue):
    queues = {}

    def __init__(self, name, size):
        super().__init__()
        self.size = size
        self.name = name
        Queue2.queues[name] = self

    def insert(self, value):
        if len(self.queue) == self.size:
            raise QueueOutOfRangeException("Queue is full")
        super().insert(value)

    def pop(self):
        if len(self.queue) == 0:
            print("The queue is empty")
            return None
        return super().pop()

    def is_empty(self):
        return super().is_empty()

    @classmethod
    def save(cls):
        with open("queues.txt", "w") as f:
            for name, queue in cls.queues.items():
                f.write(f"{name} {queue.size} {queue.queue}\n")

    @classmethod
    def load(cls):
        with open("queues.txt", "r") as f:
            for line in f:
                name, size, queue = line.split()
                cls(name, int(size))
                cls.queues[name].queue = eval(queue)

    def __str__(self):
        return str(self.queue)


class QueueOutOfRangeException(Exception):
    pass


# to call the class and test the methods

q1 = Queue2("q1", 2)
q1.insert(1)
q1.insert(2)
# q1.insert(3)
print(q1.__str__())
print(q1.is_empty())
print(q1.pop())
print(q1.pop())
print(q1.is_empty())
q1.insert("Ahmed")
print(q1.__str__())

Queue2.save()
Queue2.load()
print(Queue2.queues)

q2 = Queue2.queues["q1"]
print(q2.is_empty())
q2.insert("Hamdi")
print(q2.__str__())

