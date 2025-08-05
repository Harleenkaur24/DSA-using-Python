 def append(self,item):
        if self.n == self.size:
            #resize
            self.resize(self.size*2)

        self.A[self.n]=item
        self.n=self.n +1
