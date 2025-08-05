 def insert_head(self,value):
        
        #new node creation
        new_node=node(value)
        #create connection
        new_node.next=self.head
        #reassign head
        self.head=new_node
        #increment n
        self.n = self.n + 1
