#Cody Dzierzon
#1/2/19
#trivia game

import sys

def open_file(file_name, mode):
    """Open a file"""
    try:
        the_file  = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file",
              file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    try:
        line = the_file.readline()
    except:
        print("unable to  assign")
        input("press enter to exit")
    else:
        line = line.replace("/", "\n")
        return line

def next_block(the_file):
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []

    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[:-1]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

the_file  = open_file("test_file", "r")
category, question, answers, correct, explanation = next_block(the_file)
print(category)
print(question)
print(answers)
print(correct)
print(explanation)


        


    

























