from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        pass

    def act(self, environment):
        cells = self.sense(environment)
        decision, cell = self.decide(cells)

        if decision is True:
            return decision

    def __str__(self):
        return '💧'
