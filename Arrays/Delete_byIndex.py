def __delitem__(self,pos): 

        if  0<= pos < self.n:
            for i in range(pos,self.n-1):    #if correct index not given: behaving as pop 
               self.A[i]=self.A[i+1]

            self.n =self.n -1
