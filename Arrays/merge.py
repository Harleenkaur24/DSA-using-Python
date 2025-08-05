def merge(self,other):
        merged=MyList()
        while merged.size < self.n + other.n :
            merged.resize(merged.size*2)
        
        for i in range(self.n):
            merged.A[merged.n]=self.A[i]
            merged.n = merged.n+1
        
        for i in range(other.n):
            merged.A[merged.n]=other.A[i]
            merged.n = merged.n+1

        return merged
