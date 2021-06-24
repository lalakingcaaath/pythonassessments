test = float (input("Please type in your score in test no. 1: "))
test1 = float (input("Please type in your score in test no. 2: "))
test2 = float (input("Please type in your score in test no. 3: "))
test3 = float (input("Please type in your score in test no. 4: "))
test4 = float (input("Please type in your score in test no. 5: "))
def main():
    overall = test+test1+test2+test3+test4
    average = overall/5
    grade = test or test1 or test2 or test3 or test4
    calc_average(average)
    determine_grade(grade)
def calc_average(average):
    print ("Your average for the 5 test is ", average)
def determine_grade(grade):
    grades = float (input("Type in your score at any of the test: "))
    if grades >=90:
        print ("You got a number grade of 1!")
    elif grades >=80:
        print ("You got a number grade of 2!")
    elif grades >70:
        print ("You got a number grade of 3!")
    elif grades >60:
        print ("You got a number grade of 4!")
    elif grades <60:
        print ("You got a number grade of 5!")
main()
