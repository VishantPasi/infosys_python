#lex_auth_012693750719488000124

def get_count(num_list):
    count=0

    for i in range(0,len(num_list)-1):
        if num_list[i] == num_list[i+1]:
            count +=1
        

    return count

#provide different values in list and test your program
num_list=[1,2,2,3,4,4,4,10]
print(get_count(num_list))