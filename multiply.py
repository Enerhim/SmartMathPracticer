import random
import time

def accuracy(r, w):
    a = ((len(r)) / ((len(w)) + (len(r)) )) * 100
    return a
    
def mean(a):
    sum_ = 0
    for i in a:
        sum_ += i
    return int(sum_ / len(a))

def update_difficulty(a, du, dl, mtt):
    ninty_accuracy = []
    for i in a[-9:]:
        if i > 90:
            ninty_accuracy.append(i)
            
    if len(ninty_accuracy) > 8 and mtt < 5:

        if dl == du:
            du += 1
        elif dl < du:
            dl += 1
        return du, dl
    
    return du, dl
        
difficulty_upper = 1
difficulty_lower = 1

wrongset = []
correctset = []
timeset = []
accuracyset = []

qno = 1
while True:
    u = random.randint(2, 10**difficulty_upper)
    l = random.randint(2, 10**difficulty_lower)
    
    s = time.time() 
    answer = input(f"Q{qno}. What is {u} * {l}? ")
    if answer == " " or answer == "":
        continue
    e = time.time()
    tt = e-s
    qno += 1
    
    
    if answer == "stop":
        print("-----------------------------")
        print("Correct Ones: ", len(correctset))
        print("Wrong Ones: ", len(wrongset))
        try:
            totalt = 0
            for time in timeset: totalt += time
            print(f"Total Time: {totalt}")
            print(f"Average Time: {mean(timeset)}s")
            print(f"Accuracy {accuracy(correctset, wrongset)}%")
        except(ZeroDivisionError):
            print("-----------------------------")
            break
        print("-----------------------------")
        break
    else:
        if int(answer) == int(u) * int(l):
            print("Correct")
            correctset.append([u, l])    
            timeset.append(tt)    
            accuracyset.append(accuracy(correctset, wrongset))
        else:
            print("Wrong")
            wrongset.append([u, l])    
            timeset.append(tt)    
            accuracyset.append(accuracy(correctset, wrongset))
    
        if (qno + 1) % 10 == 0 and qno != 1:
            difficulty_upper, difficulty_lower = update_difficulty(accuracyset, difficulty_upper, difficulty_lower, mean(timeset))