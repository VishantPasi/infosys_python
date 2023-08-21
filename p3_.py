def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five = int(rupees_to_make/5)
    one_needed = rupees_to_make%5
    if five <= no_of_five :
        five_needed = five
    else :
         five_needed = no_of_five
     
    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five     

    if one_needed <= no_of_one:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)

make_amount(21,4,2)