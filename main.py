import io
import tkinter as tk
import pandas as pd
import generate as gen
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile

window = tk.Tk()
csvInputFlag = False

listOfQuestions = []
listOfAnswers = []
listOfDifficulties = []

file_path = ''

"""
This function takes in the name of the CSV file and adds the questions, answers, and difficulty 
levels into their respective lists.

csvFilePath: a string of the path of the CSV file
"""
def addCSVContentToLists(csvFilePath):
    file = pd.read_csv(csvFilePath)

    for item in file["Question"]:
        listOfQuestions.append(item)

    for item in file["Answer"]:
        listOfAnswers.append(item)

    for item in file["Difficulty"]:
        listOfDifficulties.append(item)

# qaList: a list of (question, answer) string pairs
# fileName: a string containing the desired file name
# returns: a text file containing the questions and answers in the list
#          of size n in the format q1, a1, q2, a2, ... qn, an

def qaListToText(qaList, fileName):
    with open(fileName + ".txt", "w") as file:
      length = len(qaList) - 1
      for qaPair in qaList:
        file.write(str(qaPair.question)+", ")
        print(str(qaPair.question))
        if qaList.index(qaPair) == length:
          file.write(str(qaPair.answer))
          print(str(qaPair.answer))
        else:
          file.write(str(qaPair.answer)+", ")
          print(str(qaPair.answer))
      file.close()

# qaList: a list of (question, answer) string pairs
# fileName: a string containing the desired file name
# returns: a text file containing the questions, answers, and difficulty in the
#          list of size n in the format q1, a1, d1, q2, a2, d2, ... qn, an, dn
# requires qaList and diffList to be same length

def qadListToText(qaList, diffList, fileName):
    print("Making text file from Q&A List...")

    with open(fileName+".txt", "w") as file:
      length = len(qaList) - 1
      for (qaPair, d) in zip(qaList, diffList):
        file.write(str(qaPair[0])+", ")
        file.write(str(qaPair[1])+", ")
        if qaList.index(qaPair) == length:
          file.write(str(d))
        else:
          file.write(str(d)+", ")
      file.close()

"""
This function takes in the path of a text file, which would have the questions, answers, and difficulty,
and then add all those items into the appropriate list; it is like for reloading saved data.

textFilePath: a string of the path of the text file
"""
def addTextContentToLists(textFilePath):
    try:
        with open(textFilePath, "r") as file:
            fileTextList = file.read().split(",")

            listOfQuestions.extend(fileTextList[0::3])
            listOfAnswers.extend(fileTextList[1::3])
            listOfDifficulties.extend(fileTextList[2::3])

            file.close()
    except IOError:
        pass

"""
This function takes in the user's input for the number of questions, desired difficulty level, and filename.
Then, the function randomizes the questions according to those arguments and generates a text file.

numQuestions: an integer for the number of questions that the user wants
difficultyLevel: a string for the user's chosen difficulty level, in lowercase letters
fileName: a string for the user's chosen text file name
"""
def randomizeAndMakeFile(numQuestions, difficultyLevel, fileName):
    print("Generating exam...")
    qaList = gen.returnExam(listOfQuestions, listOfAnswers, listOfDifficulties, numQuestions, difficultyLevel)
    print("Finished Generating Exam...")

    qaListToText(qaList, fileName)


def addToList():
    listOfQuestions.append(inputQuestion.get())
    listOfAnswers.append(inputAnswer.get())
    listOfDifficulties.append(inputDifficulty.get())
    showinfo("Message", f"Added: Q: " + str(inputQuestion.get()) + " and A: " + str(inputAnswer.get()) + " as Difficulty: " + str(inputDifficulty.get()))


def openFile():
    file_path = askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')]).name
    openFile.var = file_path
    if file_path is not None:
        addCSVContentToLists(file_path)
        csvInputFlag = True
        flagLabel.config(text="Success!")
        flagLabel = ttk.Label(window, text="Success!").grid(row=8, column=1)

        print("Ran CSV function\n")
        print(listOfQuestions)
        print(listOfAnswers)
        print(listOfDifficulties)


w_height = 700
w_width = 1000

window.geometry(str(w_width) + "x" + str(w_height))
window.title("Question Randomizer")


title = ttk.Label(window, text="Question Randomizer", font=("Times New Roman", 30)).grid(row=0,columnspan=2)

inputQuestion = tk.StringVar()
inputAnswer = tk.StringVar()
inputDifficulty = tk.StringVar()

ttk.Label(window, text="For Manually Adding: ").grid(row=1, column=0)
ttk.Label(window, text="Question").grid(row=2, column=0)
ttk.Label(window, text="Answer").grid(row=3, column=0)
ttk.Label(window, text="Difficulty").grid(row=4, column=0)
inputText1 = ttk.Entry(window,width=40, textvariable=inputQuestion).grid(row=2, column=1, pady=20)
inputText2 = ttk.Entry(window,width=40, textvariable=inputAnswer).grid(row=3, column=1, pady=20)
inputText3 = ttk.Entry(window,width=40, textvariable=inputDifficulty).grid(row=4, column=1, pady=20)


addToListbtn = ttk.Button(window, text="Add to list", width=40, command= lambda: addToList()).grid(row=5, columnspan=2, pady=20)

ttk.Label(window, text="For Adding a CSV FIle:").grid(row=6, column=0)

ttk.Label(window, text="CSV").grid(row=7, column=0)

#flagLabel = ttk.Label(window, text=("No Value Chosen" if (csvInputFlag is False) else "Success!")).grid(row=8, column=1)#won't change to success even after adding CSV

openFilebtn = ttk.Button(window, text="Choose from Computer", width=40, command=openFile).grid(row=7, column=1, pady=20)
flagLabel = ttk.Label(window, text="No CSV File Chosen").grid(row=8, column=1)

inputCSVDifficulty = tk.StringVar()
ttk.Label(window, text="Difficulty").grid(row=9, column=0)
inputTextCSVDifficulty = ttk.Entry(window,width=40, textvariable=inputCSVDifficulty).grid(row=9, column=1, pady=20)

inputNumQuestions = tk.StringVar()
ttk.Label(window, text="Number of Questions").grid(row=10, column=0)
inputTextNumQuestions = ttk.Entry(window,width=40, textvariable=inputNumQuestions).grid(row=10, column=1, pady=20)

inputFileName = tk.StringVar()
ttk.Label(window, text="New Text File Name").grid(row=11, column=0)
inputTextFileName = ttk.Entry(window,width=40, textvariable=inputFileName).grid(row=11, column=1, pady=20)


generatebtn = ttk.Button(window, text="Generate!", width=40, command= lambda: randomizeAndMakeFile(inputNumQuestions, inputCSVDifficulty, )
 ).grid(row=12, columnspan=2, pady=20)

window.mainloop()
