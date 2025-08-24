princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya"]

for i in range(len(princesses)):
    if i < len(princesses) - 1:
        print(princesses[i], end=", ")
    else:
        print(princesses[i])
