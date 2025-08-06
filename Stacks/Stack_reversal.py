def reverse_Stack(text):
    s=stack()
    for i in text:
        s.push(i)

    result=" "
    while(not s.isempty()):
        result= result + s.pop()

    print(result)
