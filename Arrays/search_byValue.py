 def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'Value not found'
