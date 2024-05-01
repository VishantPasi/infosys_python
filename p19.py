#lex_auth_01269437590597632045

def find_number_of_combination(number_of_flavours):
    total_combination=0
    
    total_combination = 2**number_of_flavours
    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)