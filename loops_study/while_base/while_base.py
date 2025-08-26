#1. Output each letter in a word


word = "Groceries"
index = 0
while index < len(word):
    print(word[index], end="")
    index = index + 1
print()



#2. Summarize all numbers from 1 to 100 

#option 1
i = 1
total = 0
while i <= 100:
    total = total + i
    i = i + 1
print(total)

#option 2
start = 1
end = 100
sum = 0
beginning = start
while beginning <= end:
    sum = sum + beginning
    beginning = beginning + 1
print(sum)



#3. Output nombers from 1 to 10 

i = 1
while i <= 10:
    print(i)
    i = i + 1
