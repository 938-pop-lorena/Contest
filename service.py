from random import randint

from domain import *

"""
    ======================= A ======================
"""


def addParticipant(participants: list, parameters: list):
    """
    Add a new participant to the list.

    :param participants: The list of participants
    :param parameters: Parameters used to construct the new participant dictionary
    """
    P1Score = validScore(parameters[0])
    P2Score = validScore(parameters[1])
    P3Score = validScore(parameters[2])
    participant = createParticipant(P1Score, P2Score, P3Score)
    participants.append(participant)


def insertParticipant(participants: list, parameters: list):
    """
    Insert a participant on the given position.

    :param participants: List of participants
    :param parameters: Command parameters
    """
    pos = parameters[4]
    pos: int = validPositon(participants, pos)

    P1Score = parameters[0]
    P2Score = parameters[1]
    P3Score = parameters[2]

    participant = createParticipant(P1Score, P2Score, P3Score)
    participants.insert(pos, participant)


"""
    ========================== B ==========================
"""


def removeFromPosition(participants: list, parameters: list):
    """
    Removes a participant from the given position.

    :param participants: List of participants
    :param parameters: position
    """
    pos = parameters[0]
    pos = validPositon(participants, pos)
    participants.pop(pos)


def removeFromRange(participants: list, parameters: list):
    """
    Sets the scores of participants between given positions to 0,

    :param participants: List of participants
    :param parameters: The positions
    """
    startPos = validPositon(participants, parameters[0])
    endPos = validPositon(participants, parameters[2])
    for i in range(startPos, endPos + 1):
        setP1(participants[i], 0)
        setP2(participants[i], 0)
        setP3(participants[i], 0)


def replaceScore(participants: list, parameters: list):
    """
    For the given participant, replace the old score of a problem with the new one.

    :param participants: List of participants
    :param parameters: List of parameters
    :return:
    """
    participantPos = validPositon(participants, parameters[0])
    problem = validProblemNumber(parameters[1])
    newScore = validScore(parameters[3])
    if problem == "P1":
        setP1(participants[participantPos], newScore)
    elif problem == "P2":
        setP2(participants[participantPos], newScore)
    else:
        setP3(participants[participantPos], newScore)


"""
    ========================== C ==========================
"""


def listParticipants(participants: list):
    """
    Lists all the participants.

    :param participants: The list to be printed
    """
    for i in range(0, len(participants)):
        print(str(i) + ") " + toStr(participants[i]))


def listSorted(participants: list):
    """
    Returns a list of participants sorted in descending order by their average score.

    :param participants: The list of participants
    :return: List of sorted participants
    """
    sortedParticipants = sorted(participants, key=lambda participant: averageScore(participant), reverse=True)
    return sortedParticipants


def listAverageWithRelation(participants: list, parameters: list) -> list:
    """
    List all the participants having an average score respecting the relation.

    :param participants: List of participants
    :param parameters: List of parameters
    """
    relation = validRelation(parameters[0])
    score = valueToInteger(parameters[1])
    filteredParticipants = []
    if relation == ">":
        for participant in participants:
            if averageScore(participant) > score:
                filteredParticipants.append(participant)
    if relation == "<":
        for participant in participants:
            if averageScore(participant) < score:
                filteredParticipants.append(participant)
    if relation == "=":
        for participant in participants:
            if averageScore(participant) == score:
                filteredParticipants.append(participant)
    return filteredParticipants


"""
    ========================== D ==========================   
"""


def averageScoreInRange(participants: list, parameters: list):
    """
    Return the average score of average scores for participants in given range.

    :param participants: List of participants
    :param parameters: List of parameters
    :return: int - average score
    """
    startPos = validPositon(participants, parameters[0])
    endPos = validPositon(participants,parameters[2])
    avgSum = 0
    count = 0
    for i in range(startPos, endPos + 1):
        avgSum = avgSum + averageScore(participants[i])
        count += 1
    avg = int(avgSum/count)
    return avg


def lowestAverage(participants: list, parameters: list):
    """
    Returns the lowest average score of participants between given positions.

    :param participants: List of participants
    :param parameters: List of parameters
    :return: int - lowest average score
    """
    startPos = validPositon(participants, parameters[0])
    endPos = validPositon(participants, parameters[2])
    minScore = 10
    for i in range(startPos, endPos + 1):
        if averageScore(participants[i]) < minScore:
            minScore = averageScore(participants[i])
    return minScore


def generateRandomParticipants(count: int) -> list:
    """
    Generates a list of participants.

    :param count: The number of participants that must be generated
    :return: list of participants
    """
    participants = []
    for i in range(0, count):
        p1 = randint(0, 10)
        p2 = randint(0, 10)
        p3 = randint(0, 10)
        participant = createParticipant(p1, p2, p3)
        participants.append(participant)
    return participants
