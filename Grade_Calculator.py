#Grade Calculator
testone = input ("Please type in your score on test number 1: ")
testtwo = input ("Please type in your score on test number 2: ")
mainexam = input ("Please type in your score on the main exam: ")

if int(testone) <= 0:
    print ("Error, Please type in a valid test score")
elif int(testone) > 25
    print ("Error, Please type in a valid test score")
if int(testtwo) <= 0:
    print ("Error, Please type in a valid test score")
elif int(testtwo) >25:
    print ("Error, Please type in a valid test score")
if int(mainexam) <= 0:
    print ("Error, Please type in a valid exam score")
elif int(mainexam) >50:
    print ("Error, Please type in a valid exam score")
totalpoints = int(testone)+int(testtwo)+int(mainexam)
if int(totalpoints) >=80:
    print ("You got a grade of Distinction")
elif int(totalpoints) >=61:
    print ("You got a grade of Credit")
elif int(totalpoints) <=60:
    print ("You got a passing grade")
