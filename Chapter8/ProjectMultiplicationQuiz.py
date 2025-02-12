import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(1,numberOfQuestions+1,1):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    i=0
    start=time.time()
    while i<3:
        try:
            answer=input(prompt)
            product=int(answer)== num1*num2
        except ValueError:
            print('Incorrect')
            i+=1
            if (time.time() - start) > 8.0:
                print('Out of time!')
                break
            continue
        if product==False:
            print('Incorrect')
            i+=1 
        elif (time.time() - start) > 8.0:
            print('Out of time!')
            break   
        else:
            print('Correct!')
            correctAnswers += 1
            break
    if i==3:
        print('Out of Tries')
time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))