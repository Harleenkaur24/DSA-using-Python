def delete_head(self):

        if self.head==None:
            return "Empty LL"
        
        temp=self.head
        self.head=temp.next
        temp.next=None

        self.n =self.n -1 
