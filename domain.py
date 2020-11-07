from validation import *


def createParticipant(P1Score: int, P2Score: int, P3Score: int):
    """
    Creates a Participant dictionary from the given parameters.

    :param P1Score:
    :param P2Score:
    :param P3Score:
    :return:
    """
    P1Score = validScore(P1Score)
    P2Score = validScore(P2Score)
    P3Score = validScore(P3Score)
    participant = {"P1": P1Score,
                   "P2": P2Score,
                   "P3": P3Score}
    return participant


def getP1(participant: dict):
    return participant["P1"]


def setP1(participant: dict, value: int):
    participant["P1"] = value


def getP2(participant: dict):
    return participant["P2"]


def setP2(participant: dict, value: int):
    participant["P2"] = value


def getP3(participant: dict):
    return participant["P3"]


def setP3(participant: dict, value: int):
    participant["P3"] = value


def toStr(participant: dict):
    """
    Returns the string representation of a Participant dictionary.

    :param participant: dictionary representing a participant
    :return: str
    """
    return "P1: {}, P2: {}, P3: {}   Average: {}".format(participant["P1"],
                                                         participant["P2"],
                                                         participant["P3"],
                                                         averageScore(participant))


def averageScore(participant: dict) -> int:
    """
    Compute the average score of a participant
    :param participant: Participant for which the average score is computed
    :return: int - average score
    """
    average = (participant["P1"] + participant["P2"] + participant["P3"])/3
    average = int(average)
    return average
