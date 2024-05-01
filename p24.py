def sms_encoding(data):
  
    li = data.split()
    li_1 = []
    
   
    vowels = "aeiouAEIOU"
    for i in li:
        if len(i) == 1:
            li_1.append(i)
        else:
            temp = ""
            for j in i:
                if j not in vowels:
                    temp += j
            li_1.append(temp)
                   
    return " ".join(li_1)
data="MSD says I love cricket and tennis too"
print(sms_encoding(data))