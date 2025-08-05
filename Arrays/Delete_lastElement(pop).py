def pop(self):
        if self.n==0:
            return 'Empty list'
        
        print(self.A[self.n -1])
        self.n=self.n-1
