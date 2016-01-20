class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if self.min == [] or self.min[-1] >= x:
            self.min.append(x)

    def pop(self):
        if self.stack[-1] == self.min[-1] :
            self.min.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]