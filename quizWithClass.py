class Quiz:
    def __init__(self, quest, ans):
        self.questions = quest
        self.answers = ans
        self.count = 0

    def get_userans(self):
        for i, q in enumerate(self.questions):
            q_ans = input(q + ": ")
            if q_ans.lower() == self.answers[i].lower():
                self.count += 1
        return f"You got {self.count} out of {len(self.questions)}"

userans = Quiz(
    [ "What is the capital city of Kachin State",
      "What is the capital city of Kayin State ",
      "What is the capital city of Ayeyawady Division"],
    ["Myitkyina", "Hpa-An", "Pathein"]
)
print(userans.get_userans())