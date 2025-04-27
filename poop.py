# filename: ctoj.py
# author: Anna Chen
# username: annachen@bu.edu
# assignment: hw01
# date: 10 September 2012
# description: convert calories to joules

# input-process-output design pattern

# this is a function definition
def main():

    print ("Welcome to the energy conversion program")
    
    # collect an input
    # (the number of calories)
    # calories = 1 # "hard-coding" a value
    calorie = input ("Enter number of calories:")

    # apply some processing on the input
    # find the number of joules
    # 4.184 joules =  1 calories
    joules = float(calorie) * 4.184

    # produce an output
    print ("That's equal to", joules, "in joules.")

# this is a function call
main()




