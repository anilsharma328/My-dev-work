
laptops={"hp":20000, "dell" :40000, "Mac":120000 , "lenovo":15000 }

def laptops_price_update(element):
    return laptops[element] *2
Modified_price=list(map(laptops_price_update,laptops))
print(Modified_price)

