def myquiz(questions, correct_answers):
    correct = 0
    for i in range(len(questions)):
        user_answer = input(questions[i] + ": ")
        if user_answer.lower() == correct_answers[i].lower():
            correct += 1
    return f"You got {correct} out of {len(questions)}"


quiz_questions = ["What is the capital city of Kachin State",
                  "What is the capital city of Kayin State ",
                  "What is the capital city of Ayeyawady Division"]
quiz_answers = ["Myitkyina", "Hpa-An", "Pathein"]

print(myquiz(quiz_questions, quiz_answers))
