 
    def __getitem__(self,index):
        if 0<=index <self.n:
          return self.A[index]
        else:
            return 'IndexError -Index out of range'
