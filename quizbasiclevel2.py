def main():
    while True:
        play_quiz(quiz_questions,quiz_answers)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
def play_quiz(quiz_quest,quiz_ans):
    question_scores = [2, 3, 2, 3, 3]
    score = 0
    for i in range(len(quiz_quest)):
        user_answer = input(f"{quiz_quest[i]}: ")
        if user_answer.lower() == quiz_ans[i].lower():
            score += question_scores[i]
            print(f"Correct! You earned {question_scores[i]} points.")
        else: print(f"Incorrect. The correct answer is: {quiz_ans[i]}")
    print(f"Your total score is: {score}")
if __name__ == "__main__":
    quiz_questions = ["What is the capital city of Kachin State",
                      "What is the capital city of Kayin State ",
                      "What is the capital city of Ayeyawady Division"]
    quiz_answers = ["Myitkyina", "Hpa-An", "Pathein"]
    main()