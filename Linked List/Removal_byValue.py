def remove(self,value):

        if self.head==None:
            return 'Empty LL'
        if self.head.data == value:
            return self.delete_head()

        temp=self.head
        while(temp.next!= None):
            if temp.next.data==value:
                break
            temp=temp.next

        #case1 : item found
        #case2: item not found
        if temp.next==None:
            return 'Not found'
        else:
            temp.next=temp.next.next
