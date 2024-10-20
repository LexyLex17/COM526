from water_station import WaterStation
from robot import Robot
from flame import Flame


def is_robot(object):
    if isinstance(object, Robot):
        return True
    return False


def is_water_station(object):
    if isinstance(object, WaterStation):
        return True
    return False


def is_flame(object):
    if isinstance(object, Flame):
        return True
    return False
