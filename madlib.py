noununo = input("Enter a noun: ")
verbuno = input("Enter a verb: ")
adjuno = input("Enter an adjective: ")
noundos = input("Enter a second noun: ")
verbdos = input("Enter a second verb: ")
adjdos = input("Enter a second adjective: ")
nountres = input("Enter a third noun: ")
verbtres = input("Enter a third verb: ")

replace = int(input("Would you like to change noun #1 (1) or noun #2 (2)? Type number here:"))
if replace == 1:
    noununo = str(input("Enter new name: ").upper())
elif replace ==2:
    noundos = str(input("Enter new num: ").upper())



repeat = "Y"
while repeat == "Y":
    print("Welcome, " + noununo.upper() + "! This is a hanuted mansion. The previous owner, Mr. " + noundos.upper() + "died by " + verbuno.upper() + "in a fire. Legend says that you can hear him wailing in the walls. This " + adjuno.upper() + "house has hosted tons of A-List celebrities, such as Obama, Mark Wahlberg, and " + nountres.upper() + ". The bathrooms are currently being " + verbdos.upper() + "by our zombie staff. They don't bite. These " + adjdos.upper() + "zombies have been a part of our loyal staff for hundreds of years. This now concludes the tour of the haunted mansion. On the way out, try " + verbtres.upper() + "in our pool filled with blood. Have a nice day!")
    repeat = str(input("If you would like to play again, type Y: "))
