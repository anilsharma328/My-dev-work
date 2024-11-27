def decor_func(simple_person):
    def inner_funct(name_of_person):
        print(name_of_person," : Send the person to parlour")
        print(name_of_person,":  Person is ready for marriage")
    return inner_funct
@decor_func
def  simple_person(name_person):
    print(name_person,":this is the person in his original form")

simple_person("Anil")
