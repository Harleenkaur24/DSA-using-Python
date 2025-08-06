def undo_redo(text,pattern):
    s=stack()
    for i in text:
        s.push(i)
    
    m=stack()
    for i in pattern:
        if i=='u':
            data=s.pop()
            m.push(data)
        else:
            data =m.pop()
            s.push(data)
    
    result=""
    while(not s.isempty()):
        result= s.pop() + result 

    print(result)

