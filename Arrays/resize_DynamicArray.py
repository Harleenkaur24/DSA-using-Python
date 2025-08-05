def resize(self,new_capacity):
        #create a new array 
        B= self.create_array(new_capacity)
        self.size=new_capacity

        #copy previous content (A->B)
        for i in range(self.n):
            B[i]=self.A[i]
        
        #reassign A
        self.A=B
