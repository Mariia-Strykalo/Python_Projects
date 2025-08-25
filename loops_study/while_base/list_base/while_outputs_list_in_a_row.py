princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya"]
index = 0

while index < len(princesses):
    if index < len(princesses) - 1:
        print(princesses[index], end=", ")
    else:
        print(princesses[index])
    index = index + 1
#while <condition> → good when there is a clear end (for example, counting from 1 to 10).
i = 0
while i < 5:
    print(i)
    i += 1



princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya"]
index = 0

while True:
    if index < len(princesses) - 1:
        print(princesses[index], end=", ")
        index = index + 1
    else:
        print(princesses[index])
        break
#while True + break → good when the end depends on an event inside the loop (e.g. the user clicked "exit")
