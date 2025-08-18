students = [
    {"name": "Hermione", "house": "Gryffindor", "partronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "partronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "partronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "partronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
