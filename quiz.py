questions = ['Who founded Python?', 'What is the short version of Boolean in Python?', 
             'what is 23+71?', 'When was Python created?', 'To assign a variable do we use = or ==?']

answers = ['Guido Van Rossum', 'bool', '94', '1991', '=']

score = 0

for question in questions:
    answer = input(question + ' ')
    index = questions.index(question)
    if answer == answers[index]:
        score += 1

print(f'Thank you for playing, your score was {score} of 5')