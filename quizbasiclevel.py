def main():
    while True:
        print(play_quiz(quiz_questions, quiz_answers))
        user_response = input("Do you wanna play again? yes/no").lower()
        if user_response.lower() != "yes":
            break
def play_quiz(quest,ans):
    correct = 0
    for i in range(len(quest)):
        quest_ans = input(quest[i] + ": ")
        if quest_ans.lower() == ans[i].lower():
            correct += 1
        else:
            print(f"The correct answer is {ans[i]}")
    return f"You got {correct} out of {len(quest)}"
if __name__ == '__main__':
    quiz_questions = ["What is the capital city of Kachin State",
                      "What is the capital city of Kayin State ",
                      "What is the capital city of Ayeyawady Division"]
    quiz_answers = ["Myitkyina", "Hpa-An", "Pathein"]
    main()




"""
def main():
    while True:
        play_quiz()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

def play_quiz():
    quiz_questions = [
        "What is the capital city of Kachin State?",
        "Which river is the longest in the world?",
        "In what year did World War II end?",
        "What is the largest planet in our solar system?",
        "Who wrote the play 'Romeo and Juliet'?"
    ]
    quiz_answers = ["Myitkyina", "Nile", "1945", "Jupiter", "William Shakespeare"]

    question_scores = [2, 3, 2, 3, 3]  # Assign scores to questions

    score = 0

    for i in range(len(quiz_questions)):
        user_answer = input(f"{quiz_questions[i]}: ")

        if user_answer.lower() == quiz_answers[i].lower():
            score += question_scores[i]
            print(f"Correct! You earned {question_scores[i]} points.")
        else:
            print(f"Incorrect. The correct answer is: {quiz_answers[i]}")

    print(f"Your total score is: {score}")

if __name__ == "__main__":
    main()
 
"""

