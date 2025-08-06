def find_the_celeb(L):
    s=stack()
    for i in range(len(L)):
        s.push(i)

    while s.size() >=2:
        i=s.pop()
        j=s.pop()

        if L[i][j]==0: #i does not know j
            #j is not a celeb
            s.push(i)

        else:
            #i is not a celeb
            s.push(j)

    celeb =s.pop() #when only 1 item left


   #to confirm , check again
    for i in range(len(L)):
        if i!=celeb:
            if L[i][celeb]!=1 or L[celeb][i]!=0:
                print("no celeb")
                return
    print("celeb is",celeb)
