# Quiz Game

questions = (   "How many notes are in a scale?: ",
                "What is the standard tuning of a guitar?: ",
                "What clef does the left hand play in for piano?: ",
                "What is the acronym for the spaces of the treble clef?: ",
                "How many notes are in a chromatic scale?: ")

options = ( ("A. 12", "B. 5", "C. 7", "D. 3"), 
            ("A. DADGBE", "B. EADGBE", "C. DADGAD", "D. EGADFB"), 
            ("A. Soprano", "B. Treble", "C. Alto", "D. Bass"), 
            ("A. ACED", "B. EGDF", "C. FACE", "D. CEGD"), 
            ("A. 12", "B. 7", "C. 5", "D. 3"))

answers = ("C", "B", "D", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]}")
    question_num += 1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Score: {score}/{len(questions)}")
print()