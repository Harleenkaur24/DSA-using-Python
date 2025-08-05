def replace_max(self,value):
     if self.head==None:
        return 'Empty LL'
     temp=self.head
     max=temp
     while (temp!=None):
         if temp.data > max.data:
             max=temp
         temp=temp.next
     max.data=value 
