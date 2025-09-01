words = ["cat", "dog", "cat", "bird", "dog", "cat"]

counts = {item: words.count(item) for item in words}

print(counts)
#option for short lists



words = ["cat", "dog", "cat"]

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
#compact option for big lists, more than hundreds of thousands, for most real projects



words = ["cat", "dog", "cat"]

counts = {}
for word in words:
    if word in counts:         
        counts[word] += 1      
    else:                      
        counts[word] = 1       

print(counts)
#less comact option for hundreds of thousands but more understandable
