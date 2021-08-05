class Queue:

    def __init__(self):
        self.queue = list()

    def add_element(self, val):

        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False


    def remove_element(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is Empty")


que = Queue()
que.add_element("dennis")
que.add_element("harvish")
que.add_element("siddharth")
que.add_element("athish")

print(que)
print(que.remove_element())
print(que.remove_element())
