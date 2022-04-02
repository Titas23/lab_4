"""
This program allows a user three tries to guess the correct answer to the question
Question "What is the capitol of California", The answer is "Sacramento"

We first set max_tries * 3. Then we create a loop to iterate three times. For each iteration. 
we ask the user for the user (user imput) Then based on the answer the user gives, we check
to see if the user input matches the answer. If so, print"Correct!", then terminate the loop with a 
break statement. 

if the user could not guess the correct answer within the max_tries, then print "You have used your allotment of guesses."
Then print "The correct answer is California"
"""

"""
main 
    question = "What is the capitol of California"
    answer = "California"
    ask(question, answer)

ask 
    tries = 0 
    loop three tries
        increment tries by 1
        ask user input()
        check to "" of user input is equal to answer
            if so, print"Correct" the exit loop 
    if not correct 
        print to the user "You have used up your allotment of guesses"
        print the correct answer "The correct answer is 'California' ."

main

"""

def main():
    ## A quiz
    question = "What is the capital of California? "
    answer = "Sacramento"
    ask_question(question, answer)

def ask_question(question, answer, number_of_tries=3):
    num_tries = 0 
    while num_tries < number_of_tries:
        num_tries += 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used up your alotment of guesses.")
        print("The correct answer is", answer + '.')

main()