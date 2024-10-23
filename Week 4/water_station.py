from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for k, v in percept.items():
            if utils.is_robot(v):
                return True
        return False

    def act(self, environment):
        cells = self.sense(environment)
        decision = self.decide(cells)

        if decision:
            return decision

    def __str__(self):
        return '💧'
