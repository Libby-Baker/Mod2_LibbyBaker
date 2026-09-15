'''
Libby Baker 
Purpose of assignment: Create a function that calculates hours and minutes based on an input of minutes


Planning:
function = minutes to hours and minutes.
minutes = input = how many minutes?
minutes and hours = minutes / 60 + remainder
'''

'''
This fuction takes an imput of minutes and converts it into hours and minutes by 
dividing the input by 60, then printing those hours plus the remaining minutes
'''
def minutes_to_hours_and_minutes():
    minutes = input("How many minutes would you like to calculate?") #This line asks the user how many minutes they would like to calculate and turns their answer into a variable - minutes.
    minutes = int(minutes) #This line converts the input to an integer to ensure that it can be used in a math opperation
    hours = str(minutes//60) + (" hours") #This line converts the minutes to hours using floor division and converts it to the variable - hours. It also converts the hours to a string variable to make the final answer easy to concatonate.
    r_minutes = str(minutes%60) + (" minutes ") #This line calculates how many minutes would remain after the hours have been calculated. It also converts the remaining minutes into a string variable to make the final answer easy to concatinate.
    hours_and_minutes = hours + (", ") + r_minutes #This variable concatonates the hours and minutes into a readable output
    #This line prints the hours and minutes output
    print(hours_and_minutes)
#This line calls the function to run
minutes_to_hours_and_minutes()
    
    