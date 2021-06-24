max_temp = 102.5
temp = float(input ("Enter the new temperature: "))
while temp > max_temp:
    print ("The thermostat is too high")
    print ("Turn down the thermostat")
    print ("Wait 5 mins. and check the temperature again")
    print ("Enter the temperature again")
    temp = float(input ("Enter the new temperature: "))
print ("The temperature is acceptable")
print ("Please check again after 15 minutes")
    
    
