class Solution(object):
    def evalRPN(self, tokens):
        numStack = []
        for x in tokens:
            if x not in ['+', '-', '*', '/']:
                numStack.append(int(x))
            else:
                second, first = numStack.pop(), numStack.pop()
                numStack.append({
                            "+": (lambda: first + second),
                            "-": (lambda: first - second),
                            "*": (lambda: first * second),
                            '/': (lambda: int(float(first) / second))
                         }[x]())
        return numStack.pop()