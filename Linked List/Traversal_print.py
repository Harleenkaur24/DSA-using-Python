def find(self,value):
          
        if self.head==None:
            return 'Empty LL'
        
        temp=self.head
        pos=0
        while(temp!=None):
            if(temp.data==value):
                return pos 
            temp=temp.next
            pos = pos+1 

        return 'Not found'
