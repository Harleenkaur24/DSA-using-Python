def delete_index(self,index):
        if self.head==None:
            return 'Empty list'
        if index==0:
            return self.delete_head()
        pos=0
        temp=self.head

        while(temp.next!=None and pos<index-1):
            pos=pos+1
            temp=temp.next
            
        if temp.next==None:
           return 'Not found'
        temp.next=temp.next.next
        self.n =self.n -1 
