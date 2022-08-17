from datetime import datetime as dt, timedelta as td
import urllib.request as rq
from time import sleep
from art import *
import re

title, message = 'WORDLE CHEAT', ['Today\'s answer is:','Tomorrow\'s answer is:'] # The title and the message

def getAnswer(x=0):
    '''Get the answer'''
    jsFile = r'https://www.nytimes.com/games/wordle/main.e17c80f8.js' # The file containing the answer
    jsData = str(rq.urlopen(jsFile).read()) # Get the data from the file
    answers = jsData[jsData.index('mo=')+4:jsData.index('fo=[')-2].replace('"','').split(',') # Get the answers
    regex = r"\((?:\d+\,){6}\d+\)" # The regex to get the answer
    stDateVals = [int(val) for val in re.findall(regex, jsData)[0].replace('(','').replace(')','').split(',')] # Get the start date values
    init = dt(stDateVals[0], stDateVals[1], stDateVals[2], stDateVals[3], stDateVals[4], stDateVals[5], stDateVals[6]) + td(days=28) # Get the start date
    days = dt.today() - init # Get the number of days since the start date
    return answers[days.days + x].upper() # Get the answer

def display_ans(x=0):
    '''Display the answer'''
    answer = getAnswer(x) # Get the answer
    tprint(answer, font='block') # Display the answer
    sleep(1) # Wait for 1 second

def display_message(message):
    '''Display the message'''
    tprint(message, font='cybermedium') # Display the message
    sleep(1) # Wait for 1 second

def display_title(title):
    '''Display the title'''
    tprint(title, font='tarty1') # Display the title
    sleep(1) # Wait for 1 second

def main():

    display_title(title) # Display the title
    display_message(message[0]) # Display the message
    display_ans() # Display the answer

    if input('Do you want tomorrow\'s answer? (Y/N)').upper() == 'Y': # If the user wants tomorrow's answer
        display_message(message[1]) # Display the message
        display_ans(1) # Display the answer
        sleep(2) # Wait for 2 seconds


if __name__ == '__main__':
    main() # Run the main function