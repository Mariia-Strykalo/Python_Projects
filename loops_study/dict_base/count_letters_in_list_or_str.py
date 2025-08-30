#optiob 1
word = "banana"

counts = {item: word.count(item) for item in word}
print(counts)


#option 2
word = "banana"
counts = {}
for letter in word:
    if letter in counts:
        counts[letter] += 1 #коли буква вже в словнику, збільшуємо її значення на 1
    else:
        counts[letter] = 1 #коли зустрічаємо букву вперше, додаємо її в словник з 1
