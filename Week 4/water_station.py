from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, check, percept):
        for k, v in percept.items():
            if utils.is_robot(v):
                return True
        return False

    def act(self, environment):
        decision = self.decide("robot", self.sense(environment))
        if decision:
            return decision

    def __str__(self):
        return '💧'
