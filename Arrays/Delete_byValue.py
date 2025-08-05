def remove(self,item):
        pos= self.find(item)

        if type(pos)==int:
            #delete
            self.__delitem__(pos)

        else:
            return pos #'Value not found'
