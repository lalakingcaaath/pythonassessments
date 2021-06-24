def main():
    sales = float (input("Please enter the total sales of the month: "))
    country = sales*0.05
    state = sales*0.025
    county(country)
    states(state)
    print ("The total sales tax is ", country+state)
def county(county):
    print ("The amount of county sales tax is ", county)
def states(state):
    print ("The amount of state sales tax is ", state)
main()
