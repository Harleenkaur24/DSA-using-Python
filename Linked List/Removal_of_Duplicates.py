  def remove_duplicates(self):
        self.sorted()
        temp=self.head
        while(temp!=None and temp.next!=None):
            
            if temp.data ==temp.next.data:
                temp.next=temp.next.next
                self.n =self.n -1 

            temp=temp.next
