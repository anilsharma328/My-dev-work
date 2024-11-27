
laptops={"hp":20000, "dell" :40000, "Mac":120000 , "lenovo":15000 }
user_budget=float(input("your Budget please :"))

def laptops_check(element):
    if laptops[element] <= user_budget:
        return True

shortlisted_laptops=list(filter(laptops_check,laptops))
print(shortlisted_laptops)

