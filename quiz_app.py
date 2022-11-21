# question -> choices -> correct answer

import json

# import json as list
with open('files\quiz.json', 'r') as file:
    content = file.read()

data = json.loads(content) # means load list

# build quiz
for question in data:
    print(question["question_text"])

    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, '-', alternative)

    user_answer = int(input('Insert the number of your answer: '))
    question["user_answer"] = user_answer # add the answer to the dictionary


score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question['correct_answer']:
        score = score + 1
        result = 'Correct Answer'
    else:
        result = 'Wrong Answer'
    message = f'{result} {index + 1} - Your answer was {question["user_answer"]}, correct answer is {question["correct_answer"]}'
    print(message)

print(f'{score} out of {len(data)}')