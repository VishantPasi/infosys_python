def find_max(num1, num2):
    max_num = -1
    l = []
    if(num1<num2):
        for i in range(num1+1,num2+1):
            # if (i%5==0):
            #     l.append(i)
            for j in range(num1+2,num2+1):
                if (i+j)%3==0:
                    l.append(j)
                pass
    print(l)
max_num=find_max(10,15)
print(max_num)