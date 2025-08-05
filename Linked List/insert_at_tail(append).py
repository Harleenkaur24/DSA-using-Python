def append(self,value):   #insert at tail
        new_node=node(value)
        
        if self.head==None:
            self.head=new_node
            self.n =self.n +1 
            return
            
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        
        temp.next=new_node
        
        self.n =self.n +1
