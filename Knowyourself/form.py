from importlib.resources import path
import sys
from tkinter import *
from tkinter import ttk
import os
from docx import Document
import glob
import os
from subprocess import Popen

from setuptools import Command

root = Tk()
# root.geometry("850x1050")

root.title("KnowYourself-A Personality Prediction System")

xPadding = 10
yPadding = 10

# For scrolling:
container = ttk.Frame(root)
canvas = Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
frame = ttk.Frame(canvas)
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


def saveForm():
    # Getting answers, and adding it to the list, upon pressing save button.
    answers = []
    answers.append("Name: " + "\n" + name1.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Gender: {} ".format(a1.get()) + "\n")
    answers.append("\n"+"Phone Number: " + "\n" + PhoneNO.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"EmailAddress: " + "\n" + EmailADD.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Address: " + "\n" + RAddress.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Educaton: " + "\n" + a2.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Experiance: " + "\n" + a10.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Long-term goals: " + "\n" + a3.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Technical skills: " + "\n" + a4.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Hobbie: " + "\n" + a5.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Leadership: " + "\n" + a6.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Non Technical skills: " + a7.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Co-curricular: " + "\n" + a8.get("1.0", "end-1c") + "\n")
    answers.append("\n"+"Achievements/Accomplishments: " + "\n" + a9.get("1.0", "end-1c") + "\n")
    str1 = ""

    for abc in answers:
        str1 += abc

    f = open("test.txt", "w")
    sys.stdout = f
    print(*answers, sep="")
    f.close()

    f = open("test.txt", "r")

    root.destroy

    """
    docword = Document()
 
    file = 'test.txt'
 
    with open(file, 'r', encoding='utf-8') as openfile:
        lineword = openfile.read
        docword.add_paragrap(lineword)
        docword.save(file + ".docx")
    
    os.system(file + "docx")"""


# Name
Label(frame, text="Enter Your Name:").pack(padx=xPadding, pady=yPadding)
name1 = Text(frame, width=50, height=4)
name1.pack(padx=xPadding, pady=yPadding)

# PhoneNo.
Label(frame, text="Enter Your PhoneNo:").pack(padx=xPadding, pady=yPadding)
PhoneNO = Text(frame, width=50, height=4)
PhoneNO.pack(padx=xPadding, pady=yPadding)

# Email Address
Label(frame, text="Enter Your Email:").pack(padx=xPadding, pady=yPadding)
EmailADD = Text(frame, width=50, height=4)
EmailADD.pack(padx=xPadding, pady=yPadding)

# Address
Label(frame, text="Enter Your Residential Address:").pack(padx=xPadding, pady=yPadding)
RAddress = Text(frame, width=50, height=4)
RAddress.pack(padx=xPadding, pady=yPadding)


# Q1
Label(frame, text="Please select your gender:").pack(padx=xPadding, pady=yPadding)
a1 = StringVar(frame, "Male")
# Dictionary to create multiple buttons
genders = {
    "Male": "Male",
    "Female": "Female",
    "Others": "Others",
}
# Loop to create multiple Radiobuttons
for (text, value) in genders.items():
    Radiobutton(frame, text=text, variable=a1, value=value).pack(
        padx=xPadding,
        pady=yPadding,
    )


# Q2
Label(frame, text="Q1 What is your highest education?").pack(
    padx=xPadding, pady=yPadding
)
a2 = Text(frame, width=50, height=4)
a2.pack(padx=xPadding, pady=yPadding)

# Q3
Label(frame, text="Q2 What are your long-term goals??").pack(
    padx=xPadding, pady=yPadding
)
a3 = Text(frame, width=50, height=4)
a3.pack(padx=xPadding, pady=yPadding)

# Q4
Label(frame, text="Q3 Please enter your Technical skills:").pack(
    padx=xPadding, pady=yPadding
)
a4 = Text(frame, width=50, height=4)
a4.pack(padx=xPadding, pady=yPadding)


# Q5
Label(frame, text="Q4 What are your hobbies?").pack(padx=xPadding, pady=yPadding)
a5 = Text(frame, width=50, height=4)
a5.pack(padx=xPadding, pady=yPadding)


# Q6
Label(frame, text="Q5 Do you feel like you can lead a group of people?").pack(
    padx=xPadding, pady=yPadding
)
a6 = Text(frame, width=50, height=1)
a6.pack(padx=xPadding, pady=yPadding)


# Q7
Label(
    frame, text="Q6 Please enter your soft skils : Ex: Communication, team work, etc. ",
).pack(padx=xPadding, pady=yPadding)
a7 = Text(frame, width=50, height=4)
a7.pack(padx=xPadding, pady=yPadding)


# Q8
Label(
    frame, text="Q7 Please mention any co-curricular activities you have participated in.",
).pack(padx=xPadding, pady=yPadding)
a8 = Text(frame, width=50, height=4)
a8.pack(padx=xPadding, pady=yPadding)


# Q9
Label(frame, text="Q8	Please mention any special accomplishments/ volunteer work").pack(
    padx=xPadding, pady=yPadding
)
a9 = Text(frame, width=50, height=4)
a9.pack(padx=xPadding, pady=yPadding)

#Experiance
Label(frame, text="Q9 Work Eperiance (if not Leave Empty").pack(
    padx=xPadding, pady=yPadding
)
a10 = Text(frame, width=50, height=4)
a10.pack(padx=xPadding, pady=yPadding)

# Save button
save = Button(frame, text="Save", command=saveForm, ).pack(padx=xPadding, pady=yPadding)

# Exit buttom
#exit_button = Button(root, text="Exit", command=root.destroy)
#exit_button.pack(pady=20)


# packing all scrollbar related stuff
container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


root.mainloop()
# os.popen('doctest.py')
