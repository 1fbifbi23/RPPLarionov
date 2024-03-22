string = input("Введите строку: ")
word = ""
for i in range(len(string)):
    if string[i] != " ":
        word += string[i]
    else:
        if len(word) > 0 and word[-1] == "u":
            print(word)
        word = ""
if len(word) > 0 and word[-1] == "u":
    print(word)
else:
    print("такого слова тут нет(")