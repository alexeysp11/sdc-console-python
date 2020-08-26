"""
In this source file I am going to handle exceptions of that how user 
uses a console. 
For example, user can print "sdc -info " instead of "sdc -info", and 
both of these inputs should be identified.
"""

import sys
sys.path.append('../env')
from velocity import Velocity


def custom_or_default_data(dimension, init_velocity, accel=False):
    """
    Here we need to 1) check if user wants to enter data or set them by 
    default, 2) invoke methods of velocity module.
    
    Parameters: position, velocity, accel, time;

    """
    print(f'Dimension: {dimension}D'.upper())

    while(True):
        is_default = input('Default parameters (yes or no)? ')

        try:
            if is_default == 'y' or is_default == 'yes': 
                mock = True
                break
            
            elif is_default == 'n' or is_default == 'no':
                mock = False
                break
            
        except expression as identifier:
            pass
        
    init_data = Velocity.initialize(dimension=dimension, init_velocity=init_velocity, accel=accel, mock=mock)

    return init_data