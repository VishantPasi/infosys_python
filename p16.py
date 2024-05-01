def encode(message):
    encoded_message = ""
    count = 1

    for i in range(1, len(message)):

       
        if message[i] == message[i - 1]:

            count += 1
        else:

            encoded_message += str(count) + message[i - 1] 
            count = 1

   
    encoded_message += str(count) + message[-1] 
    return encoded_message


encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)