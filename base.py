import numpy as np
import time

class FastCalculator:
    def __init__(self, sec):
        self.time = sec
        self.answers = list()
        self.op_prob = [0.35, 0.35, 0.2, 0.1] # 0 add 1 sub 2 mul 3 div
        self.op_str = ["+", "-", "*", "/"]

    def run(self):
        answers = list()
        results = list()
        questions = list()
        operations = np.random.choice(4, 500, p=self.op_prob)

        i = 0
        t = time.time() + self.time
        while t > time.time():
            if operations[i] < 2:
                a = np.random.randint(-1000, 1000)
                b = np.random.randint(-1000, 1000)
            else:
                a = np.random.randint(-100, 100)
                b = np.random.randint(-10, 10)
            result = float(self.get_result(a, b, operations[i]))
            line = str(a) + " " + self.op_str[operations[i]] + " " + str(b) + " = "
            answer = input(line)
            if t < time.time():
                break

            results.append(result)
            answers.append(float(answer))
            questions.append(line)
            i += 1

        self.get_score(results, answers, questions)

    def get_result(self, a, b, op):
        if op == 0:
            return a+b
        elif op == 1:
            return a-b
        elif op == 2:
            return a*b
        return a/b

    def get_score(self, results, answers, questions):
        correct = 0
        for i in range(len(results)):
            if results[i] == answers[i]:
                correct += 1
        print("Answered", len(results), "question in", self.time, "seconds:", correct, "Correct")

        #LOG

        for i in range(len(results)):
            if results[i] == answers[i]:
                print("T", questions[i], results[i])
            else:
                print("F", questions[i], results[i], "answered", answers[i])

secs = input("Enter time limit in seconds: ")
calculator = FastCalculator(int(secs))
calculator.run()