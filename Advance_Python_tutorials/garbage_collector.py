class Test:
    def __init__(self):
        print("created objected")
    def __del__(self):
        print("deleted object")

t1=Test()
t2=t1
t3=t1

del t1
del t2
del t3
