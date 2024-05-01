
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    
    number = 100
    for i in range(1,no_of_passengers+1):
        number+=1
        ticket_number_list.append("{a}:{b}:{c}:{d}".format(a=airline,b=source[:3],c=destination[:3],d=number))
    
    if no_of_passengers<=5:
        return ticket_number_list
    else:
        return ticket_number_list[-5:]

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))