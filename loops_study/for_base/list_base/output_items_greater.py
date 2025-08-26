#otion 1
princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana", "Raya", "Chic"]

shorter_five = [princess for princess in princesses if len(princess) > 5]

print(shorter_five)



#option 2
digits = [12, 5, 27, 67, 9]

shorter_five = [item for item in digits if item > 10]

print(shorter_five)



#option 3
digits = [12, 5, 27, 67, 9]

counts = {item: digits.count(item) for item in digits if item > 5}
print(counts)

#output: {12: 1, 27: 1, 67: 1, 9: 1}
