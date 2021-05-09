import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FcMiso:
    """
    This class takes in `distance` as an input and returns `speed` as an output. 
    """
    def __init__(self):
        ########## INPUTS ########################
        # Input Universe functions
        self.dpp = np.arange(0,101,.01)     # distance to the previous point. 
        self.dnp = np.arange(0,101,.01)     # distance to the next point
        self.angle = np.arange(-91,91,.1)   # angle of rotation
        # Input Membership Functions
        # Distance to the previous point 
        self.dpp_tooclose = fuzz.trapmf(self.dpp, [0, 0, 2, 6])
        self.dpp_close = fuzz.trapmf(self.dpp, [2, 6, 8, 12])
        self.dpp_medium = fuzz.trapmf(self.dpp, [8, 12, 16, 20])
        self.dpp_far = fuzz.trapmf(self.dpp, [16, 24, 32, 40])
        self.dpp_toofar = fuzz.trapmf(self.dpp, [32, 48, 100, 100])
        # Distance to the next point 
        self.dnp_tooclose = fuzz.trapmf(self.dnp, [0, 0, 2, 6])
        self.dnp_close = fuzz.trapmf(self.dnp, [2, 6, 8, 12])
        self.dnp_medium = fuzz.trapmf(self.dnp, [8, 12, 16, 20])
        self.dnp_far = fuzz.trapmf(self.dnp, [16, 24, 32, 40])
        self.dnp_toofar = fuzz.trapmf(self.dnp, [32, 48, 100, 100])
        # Angle of rotation 
        self.angle_verylarge_left = fuzz.trapmf(self.angle, [-90, -90, -80, -70])
        self.angle_large_left = fuzz.trapmf(self.angle, [-80, -70, -65, -55])
        self.angle_medium_left = fuzz.trapmf(self.angle, [-65, -55, -50, -40])
        self.angle_small_left = fuzz.trapmf(self.angle, [-50, -40, -35, -25])
        self.angle_verysmall_left = fuzz.trapmf(self.angle, [-35, -25, 0, 0])
        self.angle_verysmall_right = fuzz.trapmf(self.angle, [0, 0, 25, 35])
        self.angle_small_right = fuzz.trapmf(self.angle, [25, 35, 40, 50])
        self.angle_medium_right = fuzz.trapmf(self.angle, [40, 50, 55, 65])
        self.angle_large_right = fuzz.trapmf(self.angle, [55, 65, 70, 80])
        self.angle_verylarge_right = fuzz.trapmf(self.angle, [70, 80, 90, 90])

        ########## OUTPUT ########################
        # Speed
        # Output Variables Domain
        self.speed = np.arange(0,61,.01)
        # Output Membership Function 
        self.speed_toolow = fuzz.trapmf(self.speed, [0, 0, 9, 15])
        self.speed_low = fuzz.trapmf(self.speed, [9, 15, 21, 27])
        self.speed_medium = fuzz.trapmf(self.speed, [21, 27, 33, 39])
        self.speed_high = fuzz.trapmf(self.speed, [33, 39, 45, 51])
        self.speed_toohigh = fuzz.trapmf(self.speed, [45, 51, 60, 60])
    

    def dpp_category(self, dpp_in=0):
        dpp_cat_tooclose = fuzz.interp_membership(self.dpp, self.dpp_tooclose, dpp_in)
        dpp_cat_close = fuzz.interp_membership(self.dpp, self.dpp_close, dpp_in)
        dpp_cat_medium = fuzz.interp_membership(self.dpp, self.dpp_medium, dpp_in)
        dpp_cat_far = fuzz.interp_membership(self.dpp, self.dpp_far, dpp_in)
        dpp_cat_toofar = fuzz.interp_membership(self.dpp, self.dpp_toofar, dpp_in)
        
        return dict(
            tooclose=dpp_cat_tooclose, 
            close=dpp_cat_close, 
            medium=dpp_cat_medium, 
            far=dpp_cat_far, 
            toofar=dpp_cat_toofar
        )
    

    def dnp_category(self, dnp_in=0):
        dnp_cat_tooclose = fuzz.interp_membership(self.dnp, self.dnp_tooclose, dnp_in)
        dnp_cat_close = fuzz.interp_membership(self.dnp, self.dnp_close, dnp_in)
        dnp_cat_medium = fuzz.interp_membership(self.dnp, self.dnp_medium, dnp_in)
        dnp_cat_far = fuzz.interp_membership(self.dnp, self.dnp_far, dnp_in)
        dnp_cat_toofar = fuzz.interp_membership(self.dnp, self.dnp_toofar, dnp_in)
        
        return dict(
            tooclose = dnp_cat_tooclose, 
            close = dnp_cat_close, 
            medium = dnp_cat_medium, 
            far = dnp_cat_far, 
            toofar = dnp_cat_toofar
        )


    def angle_category(self, angle_in=0):
        # left angle
        angle_cat_verylarge_left = fuzz.interp_membership(
            self.angle, 
            self.angle_verylarge_left, 
            angle_in)
        angle_cat_large_left = fuzz.interp_membership(
            self.angle, 
            self.angle_large_left, 
            angle_in)
        angle_cat_medium_left = fuzz.interp_membership(
            self.angle, 
            self.angle_medium_left, 
            angle_in)
        angle_cat_small_left = fuzz.interp_membership(
            self.angle, 
            self.angle_small_left, 
            angle_in)
        angle_cat_verysmall_left = fuzz.interp_membership(
            self.angle, 
            self.angle_verysmall_left, 
            angle_in)
        
        # right angle
        angle_cat_verysmall_right = fuzz.interp_membership(
            self.angle, 
            self.angle_verysmall_right, 
            angle_in)
        angle_cat_small_right = fuzz.interp_membership(
            self.angle, 
            self.angle_small_right, 
            angle_in)
        angle_cat_medium_right = fuzz.interp_membership(
            self.angle, 
            self.angle_medium_right, 
            angle_in)
        angle_cat_large_right = fuzz.interp_membership(
            self.angle, 
            self.angle_large_right, 
            angle_in)
        angle_cat_verylarge_right = fuzz.interp_membership(
            self.angle, 
            self.angle_verylarge_right, 
            angle_in)
        
        # return statement
        return dict(
            verylarge_left = angle_cat_verylarge_left, 
            large_left = angle_cat_large_left, 
            medium_left = angle_cat_medium_left, 
            small_left = angle_cat_small_left, 
            verysmall_left = angle_cat_verysmall_left,
            verysmall_right = angle_cat_verysmall_right,
            small_right = angle_cat_small_right,
            medium_right = angle_cat_medium_right,
            large_right = angle_cat_large_right,
            verylarge_right = angle_cat_verylarge_right
        )

        
    def inference(self, dpp_in=0, dnp_in=0, angle_in=0):
        # Apply Fuzzy inputs to membership functions
        dpp_cat_in = self.dpp_category(dpp_in)
        dnp_cat_in = self.dnp_category(dnp_in)
        angle_cat_in = self.angle_category(angle_in)

        ########## RULES ########################
        # Determine the weight for each rule from fuzzy antecents
        # IF part
        # rules that depend on distance variables
        rule_toolowspeed_distance = np.fmax(
            # avoid high speed if a car is too close to previous point
            np.fmax(
                np.fmax(
                    np.fmin(dpp_cat_in['tooclose'], dnp_cat_in['tooclose']), 
                    np.fmax(
                        np.fmin(dpp_cat_in['tooclose'], dnp_cat_in['close']), 
                        np.fmin(dpp_cat_in['tooclose'], dnp_cat_in['medium'])
                    )
                ), 
                np.fmax(
                    np.fmin(dpp_cat_in['tooclose'], dnp_cat_in['far']), 
                    np.fmin(dpp_cat_in['tooclose'], dnp_cat_in['toofar'])
                )
            ),
            # avoid high speed if a car is too close to the next point
            np.fmax(
                np.fmax(
                    np.fmin(dpp_cat_in['tooclose'], dnp_cat_in['tooclose']),
                    np.fmax(
                        np.fmin(dpp_cat_in['close'], dnp_cat_in['tooclose']),
                        np.fmin(dpp_cat_in['medium'], dnp_cat_in['tooclose'])
                    )
                ),
                np.fmax(
                    np.fmin(dpp_cat_in['far'], dnp_cat_in['tooclose']), 
                    np.fmin(dpp_cat_in['toofar'], dnp_cat_in['tooclose'])
                )
            )
        )
        rule_lowspeed_distance = np.fmax(
            # avoid high speed if a car is close to previous point
            np.fmax(
                np.fmax(
                    np.fmin(dpp_cat_in['close'], dnp_cat_in['close']), 
                    np.fmin(dpp_cat_in['close'], dnp_cat_in['medium'])
                ),
                np.fmax(
                    np.fmin(dpp_cat_in['close'], dnp_cat_in['far']), 
                    np.fmin(dpp_cat_in['close'], dnp_cat_in['toofar'])
                )
            ), 
            # avoid high speed if a car is close to the next point
            np.fmax(
               np.fmax(
                    np.fmin(dpp_cat_in['close'], dnp_cat_in['close']), 
                    np.fmin(dpp_cat_in['medium'], dnp_cat_in['close'])
                ), 
                np.fmax(
                    np.fmin(dpp_cat_in['far'], dnp_cat_in['close']), 
                    np.fmin(dpp_cat_in['toofar'], dnp_cat_in['close'])
                ) 
            )
        )
        rule_mediumspeed_distance = np.fmax(
            # avoid high speed if a distance to the previous point is medium 
            np.fmax(
                np.fmin(dpp_cat_in['medium'], dnp_cat_in['medium']), 
                np.fmax(
                    np.fmin(dpp_cat_in['medium'], dnp_cat_in['far']), 
                    np.fmin(dpp_cat_in['medium'], dnp_cat_in['toofar'])
                )
            ), 
            # avoid high speed if a distance to the next point is medium 
            np.fmax(
                np.fmin(dpp_cat_in['medium'], dnp_cat_in['medium']), 
                np.fmax(
                    np.fmin(dpp_cat_in['far'], dnp_cat_in['medium']), 
                    np.fmin(dpp_cat_in['toofar'], dnp_cat_in['medium'])
                )
            )
        )
        rule_highspeed_distance = np.fmax(
            # avoid too high speed if a car is far to the previous point
            np.fmax(
                np.fmin(dpp_cat_in['far'], dnp_cat_in['far']), 
                np.fmin(dpp_cat_in['far'], dnp_cat_in['toofar'])
            ), 
            # avoid too high speed if a car is far to the next point
            np.fmax(
                np.fmin(dpp_cat_in['far'], dnp_cat_in['far']), 
                np.fmin(dpp_cat_in['toofar'], dnp_cat_in['far'])
            )
        )
        rule_toohighspeed_distance = np.fmin(
            dpp_cat_in['toofar'], 
            dnp_cat_in['toofar']
        )

        # rules that depend on angle variable
        rule_toolowspeed_angle = np.fmax(
            np.fmax(
                angle_cat_in['verylarge_left'], 
                angle_cat_in['verylarge_right']
            ), 
            np.fmax(
                angle_cat_in['large_left'], 
                angle_cat_in['large_left']
            )
        ) 
        rule_lowspeed_angle = np.fmax(
            np.fmax(
                angle_cat_in['medium_left'], 
                angle_cat_in['medium_right']
            ), 
            np.fmax(
                angle_cat_in['small_left'], 
                angle_cat_in['small_right']
            )
        )
        rule_highspeed_angle = np.fmax(
            angle_cat_in['verysmall_left'],
            angle_cat_in['verysmall_right']
        ) 

        # combine rules 
        rule_toolowspeed = np.fmax(rule_toolowspeed_distance, rule_toolowspeed_angle)
        rule_lowspeed = np.fmax(rule_lowspeed_distance, rule_lowspeed_angle)
        rule_mediumspeed = rule_toolowspeed_distance
        rule_highspeed = np.fmax(rule_toolowspeed_distance, rule_toolowspeed_angle)
        rule_toohighspeed = rule_toohighspeed_distance

        # Apply implication opetator (Mamdami - min)
        # THEN part
        imp1 = np.fmin(rule_toolowspeed, self.speed_toolow)
        imp2 = np.fmin(rule_lowspeed, self.speed_low)
        imp3 = np.fmin(rule_mediumspeed, self.speed_medium)
        imp4 = np.fmin(rule_highspeed, self.speed_high)
        imp5 = np.fmin(rule_toohighspeed, self.speed_toohigh)
        
        # Aggregate all output - max
        aggregate_membership = np.fmax(
            np.fmax(imp1, imp2), 
            np.fmax(imp3, np.fmax(imp4, imp5)
            )
        )

        result_speed = fuzz.defuzz(self.speed, aggregate_membership, 'mom')
        return result_speed

