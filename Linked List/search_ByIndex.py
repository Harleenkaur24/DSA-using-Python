def __getitem__(self,index):
        if self.head==None:
            return 'Empty LL'
        
        pos=0
        temp=self.head
        while(temp!=None):
            if pos==index:
                return temp.data
            pos=pos+1
            temp=temp.next

        return 'Not index'
