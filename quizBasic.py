quiz_questions = ["What is the capital city of Kachin State",
                  "What is the capital city of Kayin State ",
                  "What is the capital city of Ayeyawady Division"]
quiz_answers = ["Myitkyina", "Hpa-An", "Pathein"]

correct = 0

for index, quest in enumerate(quiz_questions):#enumerate အစား range ကိုသုံးလည်းရ

    user_answer = input(quest + ": ")
    if user_answer.lower() == quiz_answers[index].lower():
        correct += 1

print(f"You got {correct} out of {len(quiz_questions)}")
