# Create a simple quiz application using question from a dataset loaded from a CSV file.into a dictionary
# The application will ask the user a series of questions and keep track of their score.
# The application will also provide feedback on the user's performance at the end.
import csv
import random
import time
import uuid

filepath = 'quiz_questions.csv'  # Path to the CSV file containing questions
# Load questions from a CSV file into a dictionary
def load_questions(file_path):
    questionBank = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question_id = str(uuid.uuid4())
            questionBank[question_id] = {
                'question': row['question'],
                'options': [row['option1'], row['option2'], row['option3'], row['option4']],
                'answer': row['answer']
            }
    return
# You dont have to bother about the code above, it will be explicated in the next section file handling
# load questions from the CSV file to a dictionary using the function load_questions

# write a function (ask_question) to ask the user a question and get their answer
# ask_question will take two arguments, question_id and question_data
# question_id is the unique identifier for the question
# question_data is a dictionary containing the question, options, and answer
# The function will print the question and options, and ask the user for their answer
# The function will return True if the answer is correct, and False otherwise
# hint: use the input function to get the user's answer
# hint: use the random.shuffle function to shuffle the options
def ask_question(question_id, question_data):
    print(f"Question: {question_data['question']}")
    options = question_data['options']
    random.shuffle(options)  # Shuffle the options for randomness
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    user_answer = input("Your answer (1-4): ")
    return options[int(user_answer) - 1] == question_data['answer']

# The quiz will comprises of 10 questions
# if User answers 7 or more questions correctly, they will be considered as passed
# if User answers less than 7 questions correctly, they will be considered as failed
# write a function (run_quiz)to run the quiz
# run quiz will take an argument questions which is a dictionary of questions
# hint: use the random.choice function to select a random question from the dictionary
# hint: use the time module to measure the time taken to complete the quiz
def run_quiz(questions):
    score = 0
    total_questions = 10
    start_time = time.time()
    
    for _ in range(total_questions):
        question_id, question_data = random.choice(list(questions.items()))
        if ask_question(question_id, question_data):
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {question_data['answer']}")
        print()

    end_time = time.time()
    elapsed_time = end_time - start_time
    return score, elapsed_time

# Main function to run the quiz application
def main():
    questions = load_questions(filepath)
    score, elapsed_time = run_quiz(questions)
    
    print(f"Your score: {score}/{10}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    
    if score >= 7:
        print("Congratulations! You passed the quiz.")
    else:
        print("Sorry, you failed the quiz. Better luck next time!")

main()