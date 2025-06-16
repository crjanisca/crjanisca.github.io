text = open('text.txt')
for line in text:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)