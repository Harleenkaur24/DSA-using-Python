def min(self):
        self.A=self.sort()
        return self.A[0]
    
    def max(self):
        self.A=self.sort()
        return self.A[self.n -1]
