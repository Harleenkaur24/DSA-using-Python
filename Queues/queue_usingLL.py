class queue:
    
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        new_node=node(value)

        if self.rear==None:   #when no item in queue
            self.front=new_node
            self.rear=self.front
        else:
            self.rear.next =new_node
            self.rear=new_node

    def dequeue(self):
        if self.front==None:
            return 'Empty queue'
        else:
            self.front=self.front.next

    def traversal(self):
        if self.front==None:
            return 'Empty queue'
        else:
            temp=self.front
            while(temp !=None):
                print(temp.data, end=' ')
                temp=temp.next

    def isempty(self):
        if self.front==None:
            return True
        return False
    
    def size(self):
        temp=self.front
        cnt=0

        while temp!=None:
            cnt+=1
            temp=temp.next

        return cnt
    
    def front_item(self):
        if self.front==None:
            return 'Empty queue'
        else:
            return self.front.data
        
    def rear_item(self):
        if self.front==None:
            return 'Empty queue'
        else:
            return self.rear.data
