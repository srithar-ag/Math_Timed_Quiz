import random
import time

def generate_question(level):
    if level == 1:  # Easy
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-"])
        
    elif level == 2:  # Medium
        a = random.randint(10, 50)
        b = random.randint(1, 20)
        op = random.choice(["+", "-", "*"])
        
    else:  # Hard
        a = random.randint(20, 100)
        b = random.randint(1, 20)
        op = random.choice(["*", "/"])

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "*":
        answer = a * b
    else:
        answer = round(a / b, 2)

    question = f"{a} {op} {b}"
    return question, answer


def math_quiz():
    print("🧮 Welcome to the Math Quiz Program")
    print("Select Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level = int(input("Enter difficulty level (1-3): "))

    total_questions = 5
    correct = 0
    total_time = 0

    for i in range(total_questions):
        question, answer = generate_question(level)

        print(f"\nQuestion {i+1}: {question}")

        start = time.time()
        user_answer = float(input("Your answer: "))
        end = time.time()

        response_time = end - start
        total_time += response_time

        if abs(user_answer - answer) < 0.01:
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Wrong! Correct answer: {answer}")

        print(f"⏱ Response Time: {round(response_time,2)} seconds")

    accuracy = (correct / total_questions) * 100

    print("\n📊 Quiz Summary")
    print("Total Questions:", total_questions)
    print("Correct Answers:", correct)
    print("Accuracy:", round(accuracy,2), "%")
    print("Total Time:", round(total_time,2), "seconds")
    print("Average Time:", round(total_time/total_questions,2), "seconds")


math_quiz()