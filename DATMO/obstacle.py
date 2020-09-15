"""
This class is going to generate borders of obstacles.

NOTE: 
- Try to use numpy in order to plot multiline.
"""

import numpy as np

class Obstacle: 
    def borders(self):
        upper_line = np.array([[-60,15], [-50,15], [-50,60], [5,60], [5,5], [30,5], [30,35], [50,35]])
        lower_line = np.array([[-60,-10], [-20,-10], [-20,-15], [50,-15]])
        env = [upper_line, lower_line]
        
        auto = np.array([0,0])
        
        return env, auto
