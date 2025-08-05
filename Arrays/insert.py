 def insert(self,pos,item):
        if self.n == self.size:
            self.resize(self.size*2)

        for i in range(self.n, pos,-1): #as it is backward loop 
                self.A[i]= self.A[i-1]

        self.A[pos]=item
        self.n =self.n +1 
