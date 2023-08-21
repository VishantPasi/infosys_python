def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    if (account_number<999 or account_number>2000) or (account_balance < 100000 or salary<25000):
        if (account_number<999 or account_number>2000) : 
            print("Invalid account number")
        elif (salary<25000):
            print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
        
    elif salary>=25000:

        if (salary > 25000 and salary <= 50000) and customer_emi_expected <= 36 and loan_amount_expected<=500000 :
            if (salary > 25000 and salary <= 50000) and customer_emi_expected <= 36 and loan_amount_expected<=500000 and loan_type == "Car":
            
                    eligible_loan_amount=500000
                    bank_emi_expected=36

                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
            else:
                print("Invalid loan type or salary")

        
        

        
        elif (salary > 50000 and salary < 75000) and customer_emi_expected <= 60 and loan_amount_expected<=6000000 :
            if (salary > 50000 and salary < 75000) and customer_emi_expected <= 60 and loan_amount_expected<=6000000 and loan_type == "House":
                    eligible_loan_amount=6000000
                    bank_emi_expected=60
        

                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
            else:
                print("Invalid loan type or salary")
        


        elif salary >= 75000 and customer_emi_expected <= 84 and loan_amount_expected<=7500000 :
            if salary >= 75000 and customer_emi_expected <= 84 and loan_amount_expected<=7500000 and loan_type == "Business": 
                eligible_loan_amount=7500000
                bank_emi_expected=84

                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected) 
            else:
               print("Invalid loan type or salary")
        else:
            print("Invalid loan type or salary")
        
    else:
        print("The customer is not eligible for the loan")


    
    



    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1005,20000,255000,"Car",300000,30)


