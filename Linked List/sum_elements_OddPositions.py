def oddSum(self):
        temp=self.head
        pos=0
        sum=0
        if self.head==None:
            return 'Empty LL'
        
        while(temp!=None):
            if(pos%2!=0):
                sum=sum +temp.data
            pos=pos+1
            temp=temp.next

        return sum
