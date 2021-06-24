#WiFi Three
print ("Reboot the computer and try to connect.\n(Y/N) Enter Yes or No.")
user = input("Did that fix the problem? ")
if user == "Yes" or user == "yes" or user == "No" or user == "no":
    if user == "No" or user == "no":
        print ("Reboot the router and try to connect")
        user = input("Did that fix the problem? ")
        if user == "Yes" or user == "yes" or user == "No" or user == "no":
            if user == "No" or user == "no":
                print("Make sure the cables between the router and modem are plugged firmly")
                user =input("Did that fix the problem? ")
            if user == "Yes" or user == "yes" or user == "No" or user == "no":
                if user == "No" or user == "no":
                    print ("Move the router to a new location")
                    user = input("Did that fix the problem? ")
                if user == "Yes" or user == "yes" or user == "No" or user == "no":
                    if user == "No" or user == "no":
                         print ("Get a new router")
                    else:
                         print("Please enter \"Yes\" or \"No\".\n Rerun and try again.")
                else:
                    print("Please enter \"Yes\" or \"No\".\n Rerun and try again.")
            else:
                print("Please enter \"Yes\" or \"No\".\n Rerun and try again.")
        else:
            print("Please enter \"Yes\" or \"No\".\n Rerun and try again.")
    else:
        print("Please enter \"Yes\" or \"No\".\n Rerun and try again.")
else:
    print("Please enter \"Yes\" or \"No\".\n Rerun and try again.")
                
                
                
            
 
        
    
                    
                
                         
                
        
        
