print("hello, this is program to read write into txt files ")

try:
    file=open(r"/Advance_Python_tutorials/test_file.txt", "a")
    str=input("enter Text: ")
    file.write(str +"\n")
    print(file.mode)
    print(file.name)
except FileNotFoundError as msg:
    print(msg)
finally:
    file.close()

