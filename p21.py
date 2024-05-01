def encrypt_sentence(sentence):
    li= sentence.split(" ")
    curr_word = []
    
    vowels_li = "aeiouAEIOU"
    l = ""
    for i in range(len(li)): 
        if i%2 == 0 :
            curr_word.append("".join(reversed(li[i])))
        else :
            v = []
            t = []
            for j in li[i]:
                if j not in vowels_li:
                    t.append(j)
                else:
                    v.append(j)
            t.extend(v)
            curr_word.append("".join(t))

    return " ".join(curr_word) 

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)