#Simulator Function  (and print function)
import monty_hall_simulator

#Imported for progress bar functionality
import time
import sys


# This will Welcome the user,
# Ask them for input:
#        1.Number of simulations
#        2.Contestant switching everytime or not at all.
# Print information to user.
# Run appropriate Simulations


def get_input():
    try:
        plays = int(input("How many simulations would you like to perform? (default 1000)\n> "))
    except:
        plays = 1000

    if(plays < 1):
        plays = 1000

    try:
        switchInput = raw_input("Would you like the Contestant to switch their choice?(y/n) (default yes)\n> ")
    except:
        switchInput = "y"

    if(switchInput == "n"):
        switch = False
    else:
        switch = True

    return(plays, switch)

def run_simulations(plays, switch):
    toolbar_width = 40
    printPlays = False
    wins = 0.0

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in xrange(toolbar_width):
        for j in range(plays):
            if (monty_hall_simulator.monty_hall(switch, printPlays)):
                wins += 1
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("\n")
    print("Win percentage was " + str(wins/plays/toolbar_width*100) + "%")


print("Welcome To Monty-Hall-Simulator!")
simulationInput = get_input()
print("Running monty_hall_simulator with " + str(simulationInput[0]) + " simulations. \nContestant choice switching is set to " + str(simulationInput[1]))
run_simulations(simulationInput[0], simulationInput[1])
