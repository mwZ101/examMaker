import random


# This is a class to create an question answer pair object.
class QnA_Pair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


# questionList: the list of questions
# answerList: the list of answer
# difficultyList: the list of difficulties
# numProblems: the number of problems that the user wants on the exam
# difficultyLevel: the exam difficulty level that the user wants
# returns: a list of question and answer pair
# requires questionlist, answerList, difficultyList to be of the same length

def returnExam(questionList, answerList, difficultyList, numEasyProblems, numMedProblems, numHardProblems):
    # first lets get all the indices of hard easy and medium problems

    easyQIndices = []
    medQIndices = []
    hardQIndices = []

    for i in range(len(difficultyList)):
        if difficultyList[i] == "easy":
            easyQIndices.append(i)
        elif difficultyList[i] == "medium":
            medQIndices.append(i)
        else:
            hardQIndices.append(i)

    result = []

    result+=returnEasyExam(numEasyProblems, easyQIndices, medQIndices, hardQIndices, questionList, answerList)
    result+=returnMedExam(numMedProblems, easyQIndices, medQIndices, hardQIndices, questionList, answerList)
    result+=returnHardExam(numHardProblems, easyQIndices, medQIndices, hardQIndices, questionList, answerList)

    return result


# ==============================================================================
# Easy Exam
# ==============================================================================

def returnEasyExam(numProblems, easyQIndices, medQIndices, hardQIndices, questionList, answerList):
    listOfUsedIndicesEasy = []
    listOfUsedIndicesMed = []
    listOfUsedIndicesHard = []
    listOfExamQs = []

    isEmptyEasy = len(easyQIndices) == 0
    isEmptyMed = len(medQIndices) == 0
    isEmptyHard = len(hardQIndices) == 0

    pickEasy = 0
    pickMed = 0
    pickHard = 0


    # numProb = type(int(numProblems.get()))
    numProb = numProblems - 1
    while numProb >= 0:
        while numProb >= 0 and pickEasy != 6 and not isEmptyEasy:
            randomNum = random.randrange(0, len(easyQIndices))
            if randomNum in listOfUsedIndicesEasy:
                if len(listOfUsedIndicesEasy) == len(easyQIndices):  # used up all the easies
                    pickEasy = 6
                else:
                    continue
            else:
                listOfExamQs.append(
                    QnA_Pair(questionList[easyQIndices[randomNum]], answerList[easyQIndices[randomNum]]))
                listOfUsedIndicesEasy.append(randomNum)
                numProb -= 1
                pickEasy += 1

        pickEasy = 0;

        while numProb >= 0 and pickMed != 2 and not isEmptyMed:
            randomNum = random.randrange(0, len(medQIndices))
            if randomNum in listOfUsedIndicesMed:
                if len(listOfUsedIndicesMed) == len(medQIndices):  # used up all the med
                    pickMed = 2
                else:
                    continue
            else:
                listOfExamQs.append(QnA_Pair(questionList[medQIndices[randomNum]], answerList[medQIndices[randomNum]]))
                listOfUsedIndicesMed.append(randomNum)
                numProb -= 1
                pickMed += 1

        pickMed = 0;

        while numProb >= 0 and pickHard != 1 and not isEmptyHard:
            randomNum = random.randrange(0, len(hardQIndices))
            if randomNum in listOfUsedIndicesHard:
                if len(listOfUsedIndicesHard) == len(hardQIndices):  # used up all the hard
                    pickHard = 1
                else:
                    continue
            else:
                listOfExamQs.append(
                    QnA_Pair(questionList[hardQIndices[randomNum]], answerList[hardQIndices[randomNum]]))
                listOfUsedIndicesHard.append(randomNum)
                numProb -= 1
                pickHard += 1

        pickHard = 0;
        numProb -= 1

    return listOfExamQs


# ==============================================================================
#  Medium Exam
# ==============================================================================

def returnMedExam(numProblems, easyQIndices, medQIndices, hardQIndices, questionList, answerList):
    listOfUsedIndicesEasy = []
    listOfUsedIndicesMed = []
    listOfUsedIndicesHard = []
    listOfExamQs = []

    isEmptyEasy = len(easyQIndices) == 0
    isEmptyMed = len(medQIndices) == 0
    isEmptyHard = len(hardQIndices) == 0

    pickEasy = 0
    pickMed = 0
    pickHard = 0



    # numProb = type(int(numProblems.get()))
    numProb = numProblems - 1

    while numProb >= 0:

        while numProb >= 0 and pickMed != 6 and not isEmptyMed:
            randomNum = random.randrange(0, len(medQIndices))
            if randomNum in listOfUsedIndicesMed:
                if len(listOfUsedIndicesMed) == len(medQIndices):  # used up all the med
                    pickMed = 6
                else:
                    continue
            else:
                listOfExamQs.append(QnA_Pair(questionList[medQIndices[randomNum]], answerList[medQIndices[randomNum]]))
                listOfUsedIndicesMed.append(randomNum)
                numProb -= 1
                pickMed += 1

        pickMed = 0;
        while numProb >= 0 and pickEasy != 2 and not isEmptyEasy:
            randomNum = random.randrange(0, len(easyQIndices))
            if randomNum in listOfUsedIndicesEasy:
                if len(listOfUsedIndicesEasy) == len(easyQIndices):  # used up all the easies
                    pickEasy = 2
                else:
                    continue
            else:
                listOfExamQs.append(
                    QnA_Pair(questionList[easyQIndices[randomNum]], answerList[easyQIndices[randomNum]]))
                listOfUsedIndicesEasy.append(randomNum)
                numProb -= 1
                pickEasy += 1

        pickEasy = 0;

        while numProb >= 0 and pickHard != 1 and not isEmptyHard:
            randomNum = random.randrange(0, len(hardQIndices))
            if randomNum in listOfUsedIndicesHard:
                if len(listOfUsedIndicesHard) == len(hardQIndices):  # used up all the hard
                    pickHard = 1
                else:
                    continue
            else:
                listOfExamQs.append(
                    QnA_Pair(questionList[hardQIndices[randomNum]], answerList[hardQIndices[randomNum]]))
                listOfUsedIndicesHard.append(randomNum)
                numProb -= 1
                pickHard += 1

        pickHard = 0;
        numProb -= 1

    return listOfExamQs


def returnHardExam(numProblems, easyQIndices, medQIndices, hardQIndices, questionList, answerList):
    listOfUsedIndicesEasy = []
    listOfUsedIndicesMed = []
    listOfUsedIndicesHard = []
    listOfExamQs = []

    isEmptyEasy = len(easyQIndices) == 0
    isEmptyMed = len(medQIndices) == 0
    isEmptyHard = len(hardQIndices) == 0

    pickEasy = 0
    pickMed = 0
    pickHard = 0


    # numProb = type(int(numProblems.get()))
    numProb = numProblems - 1

    while numProb >= 0:

        while numProb >= 0 and pickHard != 6 and not isEmptyHard:
            randomNum = random.randrange(0, len(hardQIndices))
            if randomNum in listOfUsedIndicesHard:
                if len(listOfUsedIndicesHard) == len(hardQIndices):  # used up all the hard
                    pickHard = 6
                else:
                    continue
            else:
                listOfExamQs.append(
                    QnA_Pair(questionList[hardQIndices[randomNum]], answerList[hardQIndices[randomNum]]))
                listOfUsedIndicesHard.append(randomNum)
                numProb -= 1
                pickHard += 1

        pickHard = 0;

        while numProb >= 0 and pickEasy != 2 and not isEmptyEasy:
            randomNum = random.randrange(0, len(easyQIndices))
            if randomNum in listOfUsedIndicesEasy:
                if len(listOfUsedIndicesEasy) == len(easyQIndices):  # used up all the easies
                    pickEasy = 2
                else:
                    continue
            else:
                listOfExamQs.append(
                    QnA_Pair(questionList[easyQIndices[randomNum]], answerList[easyQIndices[randomNum]]))
                listOfUsedIndicesEasy.append(randomNum)
                numProb -= 1
                pickEasy += 1

        pickEasy = 0;

        while numProb >= 0 and pickMed != 1 and not isEmptyMed:
            randomNum = random.randrange(0, len(medQIndices))
            if randomNum in listOfUsedIndicesMed:
                if len(listOfUsedIndicesMed) == len(medQIndices):  # used up all the med
                    pickMed = 1
                else:
                    continue
            else:
                listOfExamQs.append(QnA_Pair(questionList[medQIndices[randomNum]], answerList[medQIndices[randomNum]]))
                listOfUsedIndicesMed.append(randomNum)
                numProb -= 1
                pickMed += 1

        pickMed = 0;
        numProb -= 1

    return listOfExamQs

# ==============================================================================
# Test cases
# ==============================================================================
  
# testDiff = "hard"
# testNumProb = 11
#
# diffList = ["easy", "medium", "hard", "easy", "easy", "easy", "medium", "hard", "medium", "easy", "easy", "easy", "easy", "easy", "easy", "easy", "easy", "medium", "medium", "medium", "hard", "hard", "hard", "medium", "medium", "medium"]
# qList = ["e1", "m1", "h1", "e2", "e3", "e4", "m2", "h2", "m3", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "m3", "m4", "m5", "h3", "h4", "h5", "m6", "m7", "m8"]
# aList = ["a_e1", "a_m1", "a_h1", "a_e2", "a_e3", "a_e4", "a_m2", "a_h2", "a_m3", "a_e5", "a_e6", "a_e7", "a_e8", "a_e9", "a_e10", "a_e11", "a_e12", "a_m3", "a_m4", "a_m5", "a_h3", "a_h4", "a_h5", "a_m6", "a_m7", "a_m8"]
#
# returnedExamList = returnExam(qList, aList, diffList, testNumProb, testDiff)
#
# for qna_pairObject in returnedExamList:
#     print("[ {}, {} ]".format(qna_pairObject.question, qna_pairObject.answer))
