def sorted(self):
        temp=self.head
        values=[]   #empty list 
        while(temp!=None):
            values.append(temp.data)
            temp=temp.next

        values.sort() #sorted list

        temp=self.head  #create LL 
        for val in values:
            temp.data=val
            temp=temp.next
