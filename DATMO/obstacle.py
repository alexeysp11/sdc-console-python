"""
This class is going to generate borders of obstacles.

NOTE: 
- Try to use numpy in order to plot multiline.
"""

from shapely.geometry import LineString, MultiLineString, Point
import matplotlib.pyplot as plt

class Obstacle: 
    def borders(self):
        upper_line = MultiLineString( [[[0.0, 0.0], [7.0, 4.0]]] )
        lower_line = MultiLineString( [[[0.0, 4.0], [1.0, 5.0]]] )
        
        return (upper_line, lower_line)

if __name__ == '__main__': 
    """
    How to plot shapes?
    
    pyplot thinks that I pass two lines in one variable. 
    """
    
    obstacle = Obstacle()
    (upper_line, lower_line) = obstacle.borders()
    
    print(f'upper_line = {upper_line}')
    
    fig = plt.figure()
    
    realmap = fig.add_subplot(121)
    realmap.plot(upper_line,'b-', label='upper_line')
    realmap.plot(lower_line, 'g-', label='lower_line')
    plt.xlabel('Position X (meters)')
    plt.ylabel('Position Y (meters)')
    plt.title('Real map' , fontweight='bold')
    
    plt.grid()
    plt.legend()
    plt.show()
