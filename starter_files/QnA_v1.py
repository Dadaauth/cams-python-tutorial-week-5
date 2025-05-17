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


# The quiz will comprises of 10 questions
# if User answers 7 or more questions correctly, they will be considered as passed
# if User answers less than 7 questions correctly, they will be considered as failed
# write a function (run_quiz)to run the quiz
# run quiz will take an argument questions which is a dictionary of questions
# hint: use the random.choice function to select a random question from the dictionary
# hint: use the time module to measure the time taken to complete the quiz

# Write the main function to run the quiz application
# NB - load the questions from the CSV file to a dictionary using the function load_questions
