def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if (food_type=="N" or food_type=="n") and (quantity_ordered>=0 or quantity_ordered<=0) and (distance_in_kms>=0 or distance_in_kms<=0 ):

        if food_type=="n" or distance_in_kms<=0 or quantity_ordered<=0:
            bill_amount=-1

        elif distance_in_kms>0 and distance_in_kms<=3:
            bill_amount= 150*quantity_ordered 

        elif distance_in_kms>3 and distance_in_kms<=6:
            bill_amount= 150*quantity_ordered + ((distance_in_kms-3)*3)

        else: 
            bill_amount= 150*quantity_ordered+((distance_in_kms-6)*6)+9

    elif (food_type=="V" or food_type=="v") and (quantity_ordered>=0 or quantity_ordered<=0) and (distance_in_kms>=0 or distance_in_kms<=0 ):
        
        if food_type=="v" or distance_in_kms<=0 or quantity_ordered<=0:
            bill_amount=-1

        elif distance_in_kms>0 and distance_in_kms<=3:
            bill_amount= 120*quantity_ordered 

        elif distance_in_kms>3 and distance_in_kms<=6:
            bill_amount= 120*quantity_ordered+((distance_in_kms-3)*3)

        else: 
            bill_amount= 120*quantity_ordered+((distance_in_kms-6)*6)+9

    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("n",1,7)
print(bill_amount)