class Solution(object):
    def simplifyPath(self, path):
        path = path.split('/')
        stack = []
        for x in path:
            if x in ['', '.']:
                continue
            else:
                if x == '..':
                    stack.pop() if stack else stack
                else:
                    stack.append(x)
        return '/'+'/'.join(stack)