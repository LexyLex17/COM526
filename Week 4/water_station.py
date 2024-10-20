from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for cell in percept:
            if utils.is_robot(cell) is True:
                return True
            else:
                return False

    def act(self, environment):
        cells = self.sense(environment)
        decision = self.decide(cells)

        if decision is True:
            return decision

    def __str__(self):
        return '💧'
