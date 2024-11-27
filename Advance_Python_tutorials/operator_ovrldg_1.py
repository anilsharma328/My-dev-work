class Book:
    def __init__(self,pages):
        print("pages are ",pages)
        self.pages=pages
    def __add__(first,second):
       # return first.pages +second.pages
       return Book(first.pages + second.pages )
    #####Return an object which shows sum of two books. 
    def __str__(self):
        return "pages are {}".format( self.pages)
        
book1=Book(200)
book2=Book(400)
book3=Book(500)
book4=Book(600)


print(book1 + book2 +book3 +book4)
