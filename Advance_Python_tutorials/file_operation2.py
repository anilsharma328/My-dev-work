import os
import sys

filename=input("provide file name :")
directory=r"C:\Users\anils\PycharmProjects\pythonProject1\ "
filename=directory.strip() + filename

if(os.path.isfile( filename)):
    print("file {} exist".format(filename))
    file=open(filename,"r" )
    if(file.readable()):
        print(file.read())
    else:
        print("can not read file content ")



else:
    print("file not found",filename)
    sys.exit()