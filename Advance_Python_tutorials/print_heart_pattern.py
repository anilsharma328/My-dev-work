
for i in range(0,6):
    for j in range(0,9):
        if  i==0 and (  j ==1 or j==2 or j ==4 or j==5):
            print("*",end =" ")
        elif  i==1 and (  j ==0 or j==3 or j ==7 ):
            print("*",end =" ")
        elif  i==2 and ( j ==0 or j ==7 ):
            print("*",end =" ")
        elif  i==3 and ( j ==1 or j ==6 ):
            print("*",end =" ")
        elif  i==4 and ( j ==3 or j ==3 ):
            print("*",end =" ")
        else:
            print("", end=" ")
    print("")
