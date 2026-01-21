import sys
import json
import csv

# file_path = sys.argv[1]

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
    
def save_answers(id, question, options):
    try:
        with open(result_file, "a") as file:
            answers = csv.writer(file)
            answers.writerow(["id", "question", "options"])
    except FileExistsError:
        sys.exit()
        
def run_quiz(questions):
    print("\n" + questions["question"])
    print(f"Difficulty: {questions['difficulty']} | Category: {questions['category']}")

    for key, value in questions["options"].items():
        print(f"{key}. {value}")

    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in questions["options"]:
            return answer == questions["answer"]
        print("Invalid choice. Try again.")
                
def main_test():
    print("---- Welcome to PyQuiz -----")
    name = input("Enter your name: ").strip()

    if not name:
        sys.exit("Name cannot be empty")

    questions = loading_questions()
    run_quiz(questions)

    print("\nQuiz completed!")
        
main_test()