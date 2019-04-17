class Question:
    def __init__(self, que, c_ans):
        self.que = que
        self.c_ans = c_ans


question_list = [
    'what is your plan ?\n a)Nothing\n b)Going bangalore\n',
    'how we get the money ?\n a)Part-time-job\n b)dont know buddy\n',
]
a, b = "a", "b"
question_showing = [
    Question(que=question_list[0], c_ans=b),
    Question(que=question_list[1], c_ans=b),
]

def run_code(ques):
    score=0
    for question in ques:
        ans=input(question.que)
        if ans==question.c_ans:
            score +=1
    print(f'you scored {score} of {len(question_list)}')

run_code(question_showing)

