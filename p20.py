def find_common_characters(msg1,msg2):
    output=''
    for i in msg1:
        if i != ' ':
            if i in msg2:
                if not i in output:
                    output += i
    if output == '':
        return -1
    return output

#Provide different values for msg1,msg2 and test your program
msg1="Moto"
msg2="Moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)