class stack:
    def __init__(self,size):
        self.size=size  #we cant change size of stack
        self.stack=[None]*self.size  #stack which is an array

        self.top=-1  
   
    def push(self,value): #we cant push more than size

        if self.top==self.size -1:
            return "overfow"
        else:
            self.top+=1
            self.stack[self.top]=value
            
    def pop(self):
        if self.top==-1:
            return 'Empty stack'
        
        else:
            data=self.stack[self.top]
            self.top =self.top -1
            print(data)

    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i],end=' ')
    

    def isempty(self):
        if self.top==-1:
            return True
        return False
