def check_equal(x, y, msg=None):
    if x == y:
        if msg is not None:
            print(msg, ": Success")
    else:
        if msg is None:
            print("Error:")
        else:
            print("Error in", msg, ":")
        print("    Your answer was:", x)
        print("    Correct answer: ", y)
    assert x == y, "%r and %r are different" % (x, y)

class CountingQueue(object):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return repr(self.queue)

    def add(self, x, count=1):
        # If the element is the same as the last element, we simply
        # increment the count.  This assumes we can test equality of
        # elements.
        if len(self.queue) > 0:
            xx, cc = self.queue[-1]
            if xx == x:
                self.queue[-1] = (xx, cc + count)
            else:
                self.queue.append((x, count))
        else:
            self.queue = [(x, count)]

    def get(self):
        if len(self.queue) == 0:
            return None
        x, c = self.queue[0]
        if c == 1:
            self.queue.pop(0)
            return x
        else:
            self.queue[0] = (x, c - 1)
            return x

    def isempty(self):
        # Since the count of an element is never 0, we can just check
        # whether the queue is empty.
        return len(self.queue) == 0

def countingqueue_len(self):
    """Returns the number of elements in the queue."""
    # YOUR CODE HERE
    queue_list=[]
    for i in range(len(self.queue)):
        queue_list.extend(list(self.queue[i][0]*self.queue[i][1]))
    return len(queue_list)
# This is a way to add a method to a class once the class
# has already been defined.
CountingQueue.__len__ = countingqueue_len
        
q = CountingQueue()
for i in range(10):
    q.add('a')
q.add('b')
for i in range(3):
    q.add('c', count=2)
check_equal(len(q), 17)
