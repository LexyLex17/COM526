import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

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

# User input for the simulations (So it is different almost every time)
complexityInput = int(input(print(
    'Enter the complexity of the task from 1-10, with 10 being the hardest\n')))
timeToStudyInput = int(input(print(
    'Enter the number of weeks you have left to study the topic:\n')))

# Setting the simulation up
additionalHours_ctrl = ctrl.ControlSystem([condition1, condition2, condition3])
additionalHours_sim = ctrl.ControlSystemSimulation(additionalHours_ctrl)

additionalHours_sim.input['complexity'] = complexityInput
additionalHours_sim.input['timeToStudy'] = timeToStudyInput

additionalHours_sim.compute()

print("You should study %.2f additional hours on the subject." % additionalHours_sim.output['additionalHours'])
additionalHours.view(sim=additionalHours_sim)
