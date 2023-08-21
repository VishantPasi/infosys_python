def find_product(num1,num2,num3):
    product=0
    if num1==7:
        product=num2*num3
    elif num2==7:
        product=num3
    elif num3==7:
        product=-1
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(5,6,7)
print(product)