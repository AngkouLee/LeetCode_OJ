class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.stack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack) == 0:
            return None
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]