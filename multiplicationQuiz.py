import pyinputplus as pyp
import time
import random

numberQuestion = 10
correctAnswers = 0

for questionNumber in range(numberQuestion):
    num1 = random.randint(0, 9)
    num2 = random.randint(0,9)
    operationQues = '%s. What is the result between %s x %s?' % (questionNumber, num1, num2)
    
    # Right answers are handled by allowRegexes.
    # Wrong answers are handled by blockRegexes, with a custom message.
    try:
        pyp.inputStr(operationQues, allowRegexes=['^%s$' % (num1 * num2)],
                    blockRegexes=['.*', 'Incorrect! try again'],
                    timeout= 8, limit= 3)

    except pyp.TimeoutException:
        'Not in the correct time'

    except pyp.RetryLimitException:
        'you passed the 3 triess'
        
    else: 
        #this block runs if everything is fine
        print('Correct answer')


time.sleep(1) #brief pause to read the result
print('score: %s / %s' % (correctAnswers, numberQuestion))
