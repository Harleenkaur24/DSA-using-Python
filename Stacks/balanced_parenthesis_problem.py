def balanced_parenthesis(pattern):
    s=stack()
    
    for i in pattern:
        if i == "[" or i=="(" or i=="{":
            s.push(i)       

        else:
        
            top=s.peek()

            if (top=='[' and i==']') or \
               (top =='(' and i==')') or \
               (top=='{' and i=='}') :
                s.pop()
            else:
                return 'Mismatch'
            



    if s.isempty():
        return "Balanced"
    else:
        return "Mismatch: Stack Not Empty"
