  def sort(self):
        for i in range(self.n -1 ):
            for j in range(self.n -1 -i):
                if self.A[j]>self.A[j+1]:
                    self.swap(j,j+1)

        return self.A
    
    def swap(self,i,j):
        temp=self.A[i]
        self.A[i]=self.A[j]
        self.A[j]=temp
