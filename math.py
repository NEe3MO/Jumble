import json
import random

# Configuration
num_questions = 50   # number of generated questions
operations = ['+', '-', '*', '/']  # available operations
max_number = 50      # maximum value for generated numbers
output_file = "Math_generated.json"

questions = []

for _ in range(num_questions):
    a = random.randint(1, max_number)
    b = random.randint(1, max_number)
    op = random.choice(operations)

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
        # Ensure integer division results
        dividend = a * b
        question = f"{dividend} / {a}"
        answer = b

    questions.append({
        "q": question,
        "a": str(answer)  # store answer as string
    })

# Save to JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"✅ Generated {num_questions} math questions in {output_file}")
