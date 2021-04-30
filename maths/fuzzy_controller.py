import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyController:
    """
    This class takes in `distance` as an input and returns `speed` as an output. 
    """
    def __init__(self):
        # Declaire a domain of linguistic variables 
        self.distance = ctrl.Antecedent(np.arange(0, 101, 1), 'Distance (m)')
        self.speed = ctrl.Consequent(np.arange(0, 61, 1), 'Speed (km/h)')

        # Rename variables for more convinient usage in this method 
        distance, speed = self.distance, self.speed

        # Declaire a distance variable
        distance['Too Close'] = fuzz.trapmf(distance.universe, [0, 0, 2, 6])
        distance['Close'] = fuzz.trapmf(distance.universe, [2, 6, 8, 12])
        distance['Medium'] = fuzz.trapmf(distance.universe, [8, 12, 16, 20])
        distance['Far'] = fuzz.trapmf(distance.universe, [16, 24, 32, 40])
        distance['Too Far'] = fuzz.trapmf(distance.universe, [32, 48, 100, 100])

        # Declaire a speed variable         
        speed['Too Low'] = fuzz.trapmf(speed.universe, [0, 0, 9, 15])
        speed['Low'] = fuzz.trapmf(speed.universe, [9, 15, 21, 27])
        speed['Medium'] = fuzz.trapmf(speed.universe, [21, 27, 33, 39])
        speed['High'] = fuzz.trapmf(speed.universe, [33, 39, 45, 51])
        speed['Too High'] = fuzz.trapmf(speed.universe, [45, 51, 60, 60])

        # Declaire rules 
        rule1 = ctrl.Rule(distance ['Too Close'], speed ['Too Low'])
        rule2 = ctrl.Rule(distance ['Close'], speed ['Low'])
        rule3 = ctrl.Rule(distance ['Medium'], speed ['Medium'])
        rule4 = ctrl.Rule(distance ['Far'], speed ['High'])
        rule5 = ctrl.Rule(distance ['Too Far'], speed ['Too High'])

        # Activate rulebase
        speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])

        # Do simulaitions for getting speed value
        self.speed_simulation = ctrl.ControlSystemSimulation(speed_ctrl)


    # get distance and return speed
    def count_speed(self, entered_distance):
        self.speed_simulation.input['Distance (m)'] = entered_distance
        self.speed_simulation.compute()
        return round(self.speed_simulation.output['Speed (km/h)'], 1)
