text =  "Hello hello hello" +" "
new_word = str()
text_data = {}
for i in text:
    if i != " ":
        new_word +=i.lower()
    elif i == " ":
        if new_word in text_data:
            text_data[new_word] +=1
        elif new_word not in text_data:
            text_data[new_word] = 1
        new_word = ""

print(text_data)
