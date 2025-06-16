count = dict()
line = input("Enter sentence/paragraph\n")
words = line.split()

print("Words: ", words)
print("Counting...\n")

for word in words:
    count[word] = count.get(word,0) + 1
print("Count: ", count)
