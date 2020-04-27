import random
import os
import json
from questions import choose1, choose2, TorF
from os import system

with open('./questions/questions.json', 'r') as f:
    qaDict = json.load(f)

dict_total_q = len(qaDict)

print(
'''
    ------------------------------------------------------------------------------------------------

    Welcome to the CCNP Study Quiz App. The app is still a work in progress but is fully funtional.

    Couple things before you get started:
    1) The answers are not case sensitive
    2) True or False questions can be aswered with the words 'True' or 'False' or just 'T' or 'F'
    3) The order you enter your answers on choose 2+ or more does not matter


    Created by Mike Arrera
    ------------------------------------------------------------------------------------------------
    '''
)
print(input('Press enter to continue...\n'))
os.system('clear')

#user input for questions
while True:

    try:
        totalQ = input(f'\nHow many questions would you like to do (out of {dict_total_q})? \n\nEnter total: ')
        qaDict = random.sample(qaDict, int(totalQ))
        os.system('clear')
    except (ValueError, TypeError):
        print(f'\n!!!Please enter a number between 1 and {dict_total_q}!!!\n')
        input('\nPress ENTER to continue...')
        continue

    corrCount = 0
    totalPoss = 0
    numQ = 1

    for qa in qaDict:

        if qa['points'] == 1:
            Q = TorF(
                        question = qa['question'],
                        points = qa['points'],
                        answer = qa['answer'], 
                        category = qa['category']
                        )      

            print(str(numQ) + ". " + Q.question)
            answer = input('\nAnswer: ')
            
            corrCount += Q.check_answer(answer)
            totalPoss += Q.get_possible() #change this to pull from object instance
            numQ +=1
            os.system('clear')

        #Single Choice Questions
        if qa['points'] == 2:
            Q = choose1(
                        question= qa['question'],
                        options = qa['options'],
                        answer = qa['answer'], 
                        points = qa['points'],
                        category = qa['category']
                        )       
            print(str(numQ) + ". " + Q.question)
            print(Q.options)
            answer = input('\nAnswer: ')

            corrCount += Q.check_answer(answer)
            totalPoss += Q.get_possible()
            numQ +=1
            os.system('clear')

        #Double Choice Questions
        if qa['points'] == 3:
            Q = choose2(
                        question = qa['question'],
                        options = qa['options'],
                        answer1 = qa['answer1'],
                        answer2 = qa['answer2'], 
                        points = qa['points'],
                        category = qa['category']
                        )       
            print(str(numQ) + ". " + Q.question)
            print(Q.options)
            answer1 = input('\nAnswer #1: ')
            answer2 = input('\nAnswer #2: ')

            corrCount += Q.check_answer(answer1, answer2)
            totalPoss += Q.get_possible()
            numQ +=1
            os.system('clear')

    #figures out score
    percent = corrCount/totalPoss  
    print(f"\nYour Score: {corrCount}/{totalPoss} - " + str(format(percent, '.0%')))
    input('\nPress ENTER to exit...')
    quit()

            
