def insert_after(self,after, value):
        new_node=node(value)
        temp=self.head
        while(temp!=None):
            if temp.data==after:
                break
            temp=temp.next
        
        #case 1: break (means item found)
        if temp!=None:
            new_node.next=temp.next
            temp.next=new_node
            self.n =self.n +1 

        else:
            return 'Item not found'
        # case 2: loop completes (no item found) temp -> None
