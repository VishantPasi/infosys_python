def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if num1<(num2+num3) and num2<(num1+num3) and num3<(num1+num2):
        return (success)
    else:
        return (failure)

#Provide different values for the variables, num1, num2, num3 and test your program
num1=1
num2=7
num3=3
form_triangle(num1, num2, num3)