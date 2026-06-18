class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        if (len(self.stack)==0 and len(self.minstack)==0):
            self.stack.append(val)
            self.minstack.append(val)
        else:
            self.stack.append(val)
            if (self.minstack[-1]>=val):
                self.minstack.append(val)
        
        

    def pop(self) -> None:
        if (self.stack[-1]==self.minstack[-1]):
            self.stack.pop()
            self.minstack.pop()
        else:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
       
        
