def find_leap_years(given_year):
    li = []
    for i in range(63):
        
        if (given_year%4==0 and given_year%100 != 0) or given_year%400 == 0:
            li.append(given_year)
        given_year += 1
            

    return li[:15]

list_of_leap_years=find_leap_years(2001)
print(list_of_leap_years)


