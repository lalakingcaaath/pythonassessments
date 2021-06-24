#vineyard
R = input("The length of the row, in feet ")
E = input("The amount of space used by an end-post assembly, in feet ")
S = input("The amount of space between the vines, in feet ")
once = int(R)-2*int(E)/int(S)
print ("The number of grapevines that will fit in  the row is " + str(once))


