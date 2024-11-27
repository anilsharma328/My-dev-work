
str="bye"

for i in range(0,len(str)):          # 0,1,2
    for j in range( i+1,len(str)+1):   # 1,2,3
     print(str[i:j])     #0:1  ,0:2 , 0:3  , 1:1, 1:2,1:3 , 2:1, 2:2 ,2:3
    #  print(str[0:2])

__doc__= '''   sting 2 '''
print(__doc__)

str="Hello"
for i in range(0,len(str)):          # 0,1,2
    for j in range( i+1,len(str)+1):   # 1,2,3
     print(str[i:j])     #0:1  ,0:2 , 0:3  , 1:1, 1:2,1:3 , 2:1, 2:2 ,2:3

