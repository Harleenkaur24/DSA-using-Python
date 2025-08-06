class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def isempty(self):  #check if both stacks are empty
        if self.s1==[] and self.s2==[]:
            return True
        return False
    
    def enqueue(self,value):
        self.s1.append(value)

    def dequeue(self):
        if self.isempty():
            return 'Empty'
        
        if self.s2==[]:
            while self.s1:
                self.s2.append(self.s1.pop())

        data=self.s2.pop()
        return data    
