from agent import Agent
import utils
import random
import heapq
from environment import *


class Robot(Agent):

    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.water_level = 100
        self.water_station_location = None

    def decide(self, percept: dict[tuple[int, int], ...]):
        pass

    def act(self, environment):
        directions = {
            0 : (0, 1), # Right
            1 : (0, -1), # Left
            2 : (-1, 0), # Up
            3 : (1, 0) # Down
        }
        direction = random.randint(0,3)
        moveDirection = directions[direction]
        currentPosition = self.position
        newPosition = self.move(environment, moveDirection)
        print(currentPosition, newPosition)
        (environment.world[currentPosition[0]][currentPosition[1]], environment.world[newPosition[0]][newPosition[1]]) = (environment.world[newPosition[0]][newPosition[1]], environment.world[currentPosition[0]][currentPosition[1]])
        pass

    def move(self, environment, to):
        if environment.move_to(self.position, to, environment):
            print(self.position, to)
            xNew = self.position[1] + to[1]
            yNew = self.position[0] + to[0]
            self.position = (yNew, xNew)
            return self.position


    def __str__(self):
        return '🚒'

    # MANHATTAN DISTANCE FUNCTIONS
    def calc_path(self, start, goal, avoid):
        p_queue = []
        heapq.heappush(p_queue, (0, start))

        directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        predecessors = {start: None}
        g_values = {start: 0}

        while len(p_queue) != 0:
            current_cell = heapq.heappop(p_queue)[1]
            if current_cell == goal:
                return self.get_path(predecessors, start, goal)
            for direction in ["up", "right", "down", "left"]:
                row_offset, col_offset = directions[direction]
                neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

                if self.viable_move(neighbour[0], neighbour[1], avoid, e) and neighbour not in g_values:
                    cost = g_values[current_cell] + 1
                    g_values[neighbour] = cost
                    f_value = cost + self.calc_distance(goal, neighbour)
                    heapq.heappush(p_queue, (f_value, neighbour))
                    predecessors[neighbour] = current_cell

    def get_path(self, predecessors, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = predecessors[current]
        path.append(start)
        path.reverse()
        return path

    def viable_move(self, x, y, types, environment):
        # You will need to do this one
        # Do not move in to a cell containing an obstacle (represented by 'x')
        # Do not move in to a cell containing a flame
        # Do not move in to a cell containing a water station
        # Do not move in to a cell containing a robot.
        # In fact, the only valid cells are blank ones
        # Also, do not go out of bounds.
        print(x, y)
        if environment.world[y][x] == ' ':
            return True
        else:
            return False

    def calc_distance(self, point1: tuple[int, int], point2: tuple[int, int]):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    # END OF MANHATTAN DISTANCE FUNCTIONS


    def refill(self):
        self.water_level = 100