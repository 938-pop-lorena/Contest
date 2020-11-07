from service import *


def addUI(participants, parameters):
    if len(parameters) != 3:
        raise ValueError("Invalid parameters!")
    addParticipant(participants, parameters)


def insertUI(participants, parameters):
    if len(parameters) != 5 and parameters[4] != "at":
        raise ValueError("Invalid parameters!")
    insertParticipant(participants, parameters)


def removeUI(participants, parameters):
    if len(parameters) == 1:
        removeFromPosition(participants, parameters)
    elif len(parameters) == 2:
        removeScoreRelation(participants, parameters)
    elif len(parameters) == 3 and parameters[1] == "to":
        removeFromRange(participants, parameters)
    else:
        raise ValueError("Invalid parameters!")


def replaceUI(participants, parameters):
    if len(parameters) != 4 or parameters[2] != "with":
        raise ValueError("Invalid parameters")
    replaceScore(participants, parameters)


def listUI(participants, parameters):
    if len(parameters) == 0:
        listParticipants(participants)
    elif len(parameters) == 1 and parameters[0] == "sorted":
        listParticipants(listSorted(participants))
    elif len(parameters) == 2:
        filteredList = listAverageWithRelation(participants, parameters)
        if len(filteredList) != 0:
            listParticipants(filteredList)
        else:
            print("Nothing to show!")
    else:
        raise ValueError("Invalid parameters!")


def averageScoreUI(participants, parameters):
    if len(parameters) != 3 or parameters[1] != "to":
        raise ValueError("Invalid parameters!")
    avg = averageScoreInRange(participants, parameters)
    print(avg)


def lowestAverageUI(participants, parameters):
    if len(parameters) != 3 or parameters[1] != "to":
        raise ValueError("Invalid parameters!")
    lowestAvg = lowestAverage(participants, parameters)
    print(lowestAvg)


def topParticipantsUI(participants, parameters):
    if len(parameters) == 1:
        top = topParticipants(participants, parameters)
        listParticipants(top)
    elif len(parameters) == 2:
        top = topParticipantsForProblem(participants, parameters)
        listParticipants(top)
    else:
        raise ValueError("Invalid parameters!")


def commandName(command: str):
    command = command.strip()
    return command.split(' ')[0]


def commandParameters(command: str):
    command = command.strip()
    parameters = command.split(' ')[1:]
    if len(parameters) == 0:
        return parameters

    position = 0
    while position != len(parameters) - 1:
        parameters[position] = parameters[position].strip()
        if not parameters[position]:  # Empty string
            del parameters[position]
            position -= 1
        position += 1
    return parameters


def runConsoleUI():
    participants = generateRandomParticipants(10)

    commands = {'add': addUI,
                'insert': insertUI,
                'remove': removeUI,
                'replace': replaceUI,
                'list': listUI,
                'avg': averageScoreUI,
                'min': lowestAverageUI,
                'top': topParticipantsUI
                }

    done = False
    print("Input a command: ")
    while not done:
        command = input("> ")
        try:
            # Split command into commandName and commandParameters
            name = commandName(command)
            parameters = commandParameters(command)
            if name in commands:
                commands[name](participants, parameters)
            elif name == "exit":
                done = True
            else:
                print("Command not recognized!")
        except ValueError as ve:
            print(str(ve))
