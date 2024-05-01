def create_largest_number(number_list):
    number_list.sort(reverse=True)
    largest_number=""
    for i in range(len(number_list)):
       largest_number += str(number_list[i])
    return int(largest_number)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)