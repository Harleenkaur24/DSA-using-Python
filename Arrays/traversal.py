def __str__(self):
        result=''
        for i in range(self.n):
                result=result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

