    def extend(self,other):
        
        while self.n + other.n > self.size:
            self.resize(self.size*2)
        
        for i in range(other.n):
            self.A[self.n]=other.A[i]
            self.n = self.n +1 

        return self.A
