class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                if i=='+':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    c=b+a
                    stack.append(c)
                elif i=='-':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    c=b-a
                    stack.append(c)
                elif i=='*':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    c=a*b
                    stack.append(c)
                else:
                    a=int(stack.pop())
                    b=int(stack.pop())
                    c=int(b/a)
                    stack.append(c)
        return stack[-1]

        