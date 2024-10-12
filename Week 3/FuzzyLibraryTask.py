import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter
from tkinter import *
from tkinter import messagebox


complexity = ctrl.Antecedent(np.arange(0, 10, 1), 'complexity')
timeToStudy = ctrl.Antecedent(np.arange(0, 20, 0.5), 'timeToStudy')
additionalHours = ctrl.Consequent(np.arange(0, 20, 0.5), 'additionalHours')

# Conditions:
# i) If time is short or complexity is hard then additional study hours is high
# ii) If complexity of the task is medium then additional study hours is medium
# iii) If time is long and complexity is easy then additional study hours is low

# Complexity
complexity['easy'] = fuzz.zmf(complexity.universe, 2, 3)
complexity['medium'] = fuzz.trapmf(complexity.universe, [2, 3, 6, 7])
complexity['hard'] = fuzz.smf(complexity.universe, 6, 8)

# time left to study
timeToStudy['short'] = fuzz.zmf(timeToStudy.universe, 1, 3)
timeToStudy['medium'] = fuzz.trapmf(timeToStudy.universe, [2, 4, 5, 6])
timeToStudy['long'] = fuzz.smf(timeToStudy.universe, 5, 7)

# Additional hours
additionalHours['low'] = fuzz.zmf(additionalHours.universe, 0, 3)
additionalHours['medium'] = fuzz.trapmf(additionalHours.universe, [2, 4, 6, 7])
additionalHours['high'] = fuzz.smf(additionalHours.universe, 6, 10)

# conditions.view() # Seeing the membership functions

# Setting the conditions (rules)
condition1 = ctrl.Rule(complexity['hard'] | timeToStudy['short'], additionalHours['high'])
condition2 = ctrl.Rule(complexity['medium'], additionalHours['medium'])
condition3 = ctrl.Rule(complexity['easy'] & timeToStudy['long'], additionalHours['low'])


# Creating a GUI for the user to enter their values into

class tkinterGUI:

    def __init__(self, buttonInput):
        self.data = buttonInput


buttonInput1 = tkinterGUI(None)
buttonInput2 = tkinterGUI(None)

tk = tkinter.Tk()
tk.geometry("275x150")
e1_var = tkinter.StringVar()
e2_var = tkinter.StringVar()
e1 = Entry(tk, textvariable=e1_var)
e2 = Entry(tk, textvariable=e2_var)

def getInput(button, entry):
    button.data = entry.get()
    print(button.data)
    entry.set("")


def getOutput():
    getInput(buttonInput1, e1_var)
    getInput(buttonInput2, e2_var)
    startSim()


def startSim():
    # Setting the simulation up
    additionalHours_ctrl = ctrl.ControlSystem([condition1, condition2, condition3])
    additionalHours_sim = ctrl.ControlSystemSimulation(additionalHours_ctrl)

    additionalHours_sim.input['complexity'] = int(buttonInput1.data)
    additionalHours_sim.input['timeToStudy'] = int(buttonInput2.data)

    additionalHours_sim.compute()

    messagebox.showinfo('Result', ("Additional Study hours: %.2f" % additionalHours_sim.output['additionalHours']))


button1 = Button(tk, text='Submit', command=getOutput)
Label(tk, text='').grid(row=0)
Label(tk, text='Complexity: ').grid(row=1, column=0)
e1.grid(row=1, column=1)
Label(tk, text='').grid(row=2)
Label(tk, text='Time left to study: ').grid(row=3, column=0)
e2.grid(row=3, column=1)
Label(tk, text='').grid(row=4)
button1.grid(row=5)
Label(tk, text='').grid(row=6)
tk.mainloop()

# additionalHours.view(sim=additionalHours_sim)


