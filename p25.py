def max_frequency_word_counter(data):
    word = ""
    frequency=0
    data1 = data.lower()
    li = data1.split()

 
    word = max(li, key=li.count)
    frequency = li.count(word)

    if (frequency>1):
        print(word,frequency)
  
#Provide different values for data and test your program.
data="data-Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)
