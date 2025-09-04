#option 1
numbers = [1, 3, 4, 6, 7, 9, 10]
squares = {1: 1, 2: 4, 3: 9, 5: 25, 7: 49, 8: 64, 9: 81}

numbers_in_squares = []
for index in range(len(numbers)):
    any_number = numbers[index]
    if any_number in squares:
        numbers_in_squares.append(any_number)

print(numbers_in_squares)



#option 2
numbers = [1, 3, 4, 6, 7, 9, 10]
squares = {1: 1, 2: 4, 3: 9, 5: 25, 7: 49, 8: 64, 9: 81}

numbers_in_squares = []
for number in numbers:   # тут ми прямо беремо кожне число зі списку
    if number in squares:  # перевіряємо, чи є воно ключем у словнику
        numbers_in_squares.append(number)

print(numbers_in_squares)
