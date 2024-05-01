def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    wrong = 0

    for key,element in word_dict.items():
        if len(key) == len(element):
            flag = 0
            for k in range(0,len(key)):
                if key[k] != element[k]:
                    flag += 1
            if flag == 0:
                    correct += 1
            elif flag <= 2:
                    almost_correct += 1
            else:
                    wrong += 1
        else:
            wrong += 1
        

    return [correct,almost_correct,wrong]

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))




