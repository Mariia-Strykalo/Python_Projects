#option 1
princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya", "Chic"]
index = 0
min_length = float('inf')
shortest_word = None


while index < len(princesses):
        any_string = princesses[index]
        if min_length > len(any_string):
            min_length = len(any_string)
            shortest_word = any_string
        index = index + 1


index = 0
shortests_word = []
while index < len(princesses):
    any_word = princesses[index]
    if len(any_word) == len(shortest_word):
        shortests_word.append(any_word)
    index = index + 1


print(", ".join(shortests_word))



#option 2
princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya", "Chic"]
index = 0

min_length = len(min(princesses, key=len))

shortests_word = []
while index < len(princesses):
    any_string = princesses[index]
    if len(any_string) == min_length:
        shortests_word.append(any_string)
    index = index + 1

print(", ".join(shortests_word))
