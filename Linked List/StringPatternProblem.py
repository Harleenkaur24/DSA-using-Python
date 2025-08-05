#given a linked list of characters 
#return a new string where rules:
#1. if * or / is present -> replace by single space
#2. if 2 consecutive * or / , then repalce by single space and make the next character Capital

def modify(self):
        temp=self.head
        while temp!=None:
            if temp.data=='*' or temp.data=="/":
                temp.data=' '
                if temp.next.data=="*" or temp.next.data=='/':
                    temp.next.next.data=temp.next.next.data.upper()
                    temp.next=temp.next.next

            temp=temp.next
