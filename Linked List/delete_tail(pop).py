 def pop(self):
        temp=self.head
        #empty LL
        if self.head==None:
            return 'Empty LL'
        #if LL contains only 1 item
        if temp.next==None:
            return self.delete_head()

        while(temp.next.next !=None):
            temp= temp.next

        temp.next=None
        self.n =self.n -1 
