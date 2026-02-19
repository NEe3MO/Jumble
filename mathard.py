import json
import random
import math

# Configuration
levels = {
    "easy": {"count": 20, "max_number": 10},
    "medium": {"count": 20, "max_number": 50},
    "hard": {"count": 20, "max_number": 100}
}

# Function to generate one question
def generate_question(level):
    max_number = levels[level]["max_number"]
    a = random.randint(1, max_number)
    b = random.randint(1, max_number)
    
    # Select operation type
    ops = ['+', '-', '*', '/', '^', '√', '%', 'combo1', 'combo2', 'combo3', 'abs']
    op = random.choice(ops)
    
    # Generate question and answer
    if op == '+':
        question = f"{a} + {b}"
        answer = a + b
    elif op == '-':
        question = f"{a} - {b}"
        answer = a - b
    elif op == '*':
        question = f"{a} * {b}"
        answer = a * b
    elif op == '/':
        b = random.randint(1, max_number)  # avoid division by zero
        question = f"{a} / {b}"
        answer = round(a / b, 2)
    elif op == '^':
        question = f"{a} ^ 2"
        answer = a ** 2
    elif op == '√':
        question = f"√{a*a}"
        answer = a
    elif op == '%':
        question = f"{a} % {b}"
        answer = a % b
    elif op == 'combo1':
        c = random.randint(1, max_number)
        question = f"({a} + {b}) * {c}"
        answer = (a + b) * c
    elif op == 'combo2':
        c = random.randint(1, max_number)
        question = f"{a} * {b} - {c}"
        answer = a * b - c
    elif op == 'combo3':
        c = random.randint(1, max_number)
        question = f"({a} + {b}) / {c}"
        answer = round((a + b) / c, 2)
    elif op == 'abs':
        question = f"|{a - b}|"
        answer = abs(a - b)
    
    return {"q": question, "a": answer}

# Generate output files
for level in levels:
    questions = [generate_question(level) for _ in range(levels[level]["count"])]
    filename = f"Math_{level}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated file: {filename}, question count: {len(questions)}")
