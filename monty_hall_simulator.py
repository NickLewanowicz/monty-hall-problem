import random
###Monty Hall Simulator
# This function will generate 3 doors; one has a sports car (carDoor) behind, the other 2 goats
# The Contestant will pick a door at random (firstPick).
# One door will be revealed to having a goat behind it (showDoor).
# Contestant will either switch to the remaining door or keep their firstPick


def monty_hall(switch,printPlays):
    door = [0]*3
    timeWasted = 0

    carDoor = (random.randrange(0,3))

    firstPick = (random.randrange(0,3))

    showDoor = (random.randrange(0,3))

    while(showDoor == carDoor or showDoor == firstPick):
        timeWasted += 1
        showDoor = (random.randrange(0,3))

    door[showDoor] = 2

    if(printPlays):
        printDoors(door, carDoor, firstPick,switch)

    if(switch):
        return (carDoor != firstPick);
    else:
        return (carDoor == firstPick)

def printDoors(doors, carDoor, firstPick, switch):
    doors[carDoor] = str(doors[carDoor]) + '*'
    doors[firstPick] = str(doors[firstPick]) + '<'
    print("Switch?" + str(switch) + str(doors))
