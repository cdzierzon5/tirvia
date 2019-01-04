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

def welcome(title):
    print("\t\tWelcome to THE TRIVIA CHALLENGE!!!\n")
    print("\t\t", title, "\n")
    
def main():
    open_file("test_file.txt", "r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(answers)
        answer = input("Enter what you think the answer is: ")
        if answer == correct:
            print("nice job you got this qustion correct!")
            print(correct)
            score += 1
            print(score)
        else:
            print("you didn't get this quseion right")
            print("the correct answer was:", correct)
            print(score)
        category, question, answers, correct, explanation = next_block(the_file)
    test_file.close()
    print("you have reached the end of this test")
    print("your score is: ", score)
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

        


    

























