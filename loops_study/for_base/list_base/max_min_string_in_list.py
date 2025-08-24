#option 1
princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya", "Chic"]


def get_all_shortest_words(words_list):
    if not words_list:
        return []

    min_length = len(min(words_list, key=len))

    shortest_words = [item for item in words_list if len(item) == min_length]

    return shortest_words


result = get_all_shortest_words(princesses)
print(", ".join(result))



#option 2
princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya", "Chic"]


def min_word(list):
    min_length = len(list[0])

    for item in range(len(list)):
        if min_length > len(list[item]):
            min_length = len(list[item])
    return min_length


shortest_words = [item for item in princesses if len(item) == min_word(princesses)]


result = shortest_words
print(", ".join(result))



#option 3
princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya", "Chic"]


min_length = len(princesses[0])
for item in princesses:
    if len(item) < min_length:
        min_length = len(item)


shortest_words = []
for item in princesses:
    if len(item) == min_length:
        shortest_words.append(item)


for item in range(len(shortest_words)):
    if item < len(shortest_words) - 1:
        print(shortest_words[item], end=", ")
    else:
        print(shortest_words[item])
