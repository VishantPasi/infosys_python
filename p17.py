
#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    total_chocolates_received = 0
    for i in chocolates_received:
        total_chocolates_received += i
    
    return total_chocolates_received

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
    elif child_id_rewarded not in child_id:
        print("Child id is invalid")
    else:
        index = child_id.index(child_id_rewarded)
        chocolates_received[index] += extra_chocolates
        print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)