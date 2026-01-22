import sys
import json
import csv
import datetime
import random

if len(sys.argv) < 2:
    sys.exit("Provide the file path")

file_path = sys.argv[1]
result_file = "results.csv"


def loading_questions():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        sys.exit("File not found")
    except json.JSONDecodeError:
        sys.exit("Invalid JSON file")


def save_answers(student_id, question, selected, correct):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    write_header = False
    try:
        with open(result_file, "r"):
            pass
    except FileNotFoundError:
        write_header = True

    with open(result_file, "a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["timestamp", "id", "question", "selected", "correct"])
        writer.writerow([current_time, student_id, question, selected, correct])


def run_quiz(question, student_id):
    print("\n" + question["question"])
    print(f"Difficulty: {question['difficulty']} | Category: {question['category']}")

    for key, value in question["options"].items():
        print(f"{key}. {value}")

    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in question["options"]:
            correct = answer == question["answer"]
            save_answers(student_id, question["question"], answer, correct)
            
            return correct, answer
        print("Invalid choice. Try again.")


def main_test():
    print("---- Welcome to PyQuiz -----")
    name = input("Enter your name: ").strip()

    if not name:
        sys.exit("Name cannot be empty")

    all_questions = loading_questions()
    
    num_to_ask = 10
    if len(all_questions) >= num_to_ask:
        quiz_questions = random.sample(all_questions, num_to_ask)
    else:
        quiz_questions = all_questions
        random.shuffle(quiz_questions)

    score = 0
    incorrect_log = []

    for question in quiz_questions:
        is_correct, user_choice = run_quiz(question, name)
        
        if is_correct:
            score += 1
        else:
            # Store details of the missed question for the end report
            incorrect_log.append({
                "question": question["question"],
                "your_answer": user_choice,
                "correct_key": question["answer"],
                "correct_value": question["options"][question["answer"]]
            })

    total_q = len(quiz_questions)
    percentage = (score / total_q) * 100

    print("\n--- QUIZ COMPLETED ---")
    print(f"Final Score: {score}/{total_q}")
    print(f"Percentage:  {percentage:.2f}%")

    if incorrect_log:
        print("\n--- Review of Incorrect Answers ---")
        for item in incorrect_log:
            print(f"Q: {item['question']}")
            print(f"   You chose: {item['your_answer']}")
            print(f"   Correct Answer: {item['correct_key']}. {item['correct_value']}")
    else:
        print("\nPerfect Score! Great job!")

main_test()