class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top==None
    
    def push(self,value):
        new_node=node(value)
        temp=self.top
        new_node.next=temp
        self.top=new_node

    def traversal(self):
        temp=self.top
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    
    def peek(self):
        if(self.isempty()):
            return "Stack empty"
        else:
            return self.top.data
    
    def pop(self):
        if(self.isempty()):
            return "stack empty"
        else:
            data=self.top.data
            self.top=self.top.next
        return data

    def size(self):
        if (self.isempty()):
            return "stack empty"
        
        temp=self.top
        cnt=0
        while(temp!=None):
            cnt=cnt+1
            temp=temp.next

        return cnt
    
        
