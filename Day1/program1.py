# print the string in the format
string = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are"
print(f"{string}")

# print the version of python
import sys
print(sys.version)
print(sys.version_info)

# get the current date
import datetime
now = datetime.datetime.now()
print(now)
print ("Current date and time : ")
print (now.strftime("%d-%m-%Y %H:%M:%S"))
