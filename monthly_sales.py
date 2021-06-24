def main():
    sales = float (input("Please enter your monthly sales: "))
    advance = float (input("Please enter your advanced pay: "))
    commission = float (input("Please enter your commission rate according to your sales for the month: "))
    rate = sales*commission #monthly sale commission rate
    pay = sales*commission-advance
    commission_rate(rate)
    salary(pay)
def commission_rate(rate):
    print ("Your commission rate is ", rate)
def salary(pay):
    print ("Your pay is ", pay)
    if pay <0:
        print ("You must reimburse to the company")
main()
