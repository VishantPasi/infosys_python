def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    index = []

    for k in reqd_gems:
        if k in gems_list:
            index.append(gems_list.index(k))   
        else:
            bill_amount =-1                     

    if bill_amount != -1:
        count = 0
        for i in index[0:len(reqd_gems)]:
            bill_amount += price_list[i]*reqd_quantity[count]
            count+=1
        if bill_amount>30000:
            bill_amount = bill_amount-bill_amount*0.05

    return bill_amount

#List of gems available in the store
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[4316, 1342, 8734, 6421]

#List of gems required by the customer
reqd_gems=['Amber', 'Topaz']

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[1, 4]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)



