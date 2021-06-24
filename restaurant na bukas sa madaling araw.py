a = input ("Are you a vegetarian?.\n Yes or No: ")
b = input ("Are you a vegan?.\n Yes or No: ")
c = input ("Are you a gluten-free person?.\n Yes or No: ")
if a == "Yes" or a == "yes" or a == "no" or a == "No":
    if a == "Yes" or a == "yes":
        print ("Here are your restaurant choices.\n Main Street Pizza Company.\n Mama's Fine Italian.\n Corner Cafe.\n The Chef's Kitchen.\n")
    else:
        print ("Here are your restaurant choices.\n Joe's Gourmet Burgers")
        if b == "Yes" or b == "yes":
            print ("Here are your restaurant choices.\n Corner Cafe.\n The Chef's Kitchen")
        else:
            ("Here are your restaurant choices.\n Joe's Gourmet Burgers.\n Main Street Pizza Company.\n Mama's Fine Italian")
            if c == "Yes" or c == "yes":
               print ("Here are your restaurant choices.\n Main Street Pizza Company.\n Corner Cafe.\n The Chef's Kitchen")
            else:
                print ("Here are your restaurant choices.\n Joe's Gourmet Burgers.\n Mama's Fine Italian")
