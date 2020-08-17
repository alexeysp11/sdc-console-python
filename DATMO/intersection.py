"""
Line segments intersection. 
"""

import numpy as np
import matplotlib.pyplot as plt

class Intersection:
    def line_intersection(line1, line2):
        xdiff = (line1[0, 0] - line1[1, 0], line2[0, 0] - line2[1, 0])
        ydiff = (line1[0, 1] - line1[1, 1], line2[0, 1] - line2[1, 1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
           return None, None

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        
        point = Intersection.check_bounds(x, y, line1, line2)
        
        return point


    def check_bounds(Xa, Ya, line1, line2): 
        """
        The abcisse Xa of the potential point of intersection (Xa,Ya) must be contained in both interval I1 and I2, defined as follow :

        I1 = [min(X1,X2), max(X1,X2)]
        I2 = [min(X3,X4), max(X3,X4)]
        And we could say that Xa is included into :

        Ia = [max( min(X1,X2), min(X3,X4) ),
              min( max(X1,X2), max(X3,X4) )]
        """
        
        if((Xa >= max(min(line1[0,0], line1[1,0]), 
                      min(line2[0,0], line2[1,0])) and 
            Xa <= min(max(line1[0,0], line1[1,0]), 
                      max(line2[0,0], line2[1,0]))) and 
           (Ya >= max(min(line1[0,1], line1[1,1]), 
                      min(line2[0,1], line2[1,1])) and 
            Ya <= min(max(line1[0,1], line1[1,1]), 
                      max(line2[0,1], line2[1,1])))):
            return Xa, Ya
        else: 
            return None, None
