"""
In this source file I am going to ask user about setting default parameters
and then call initialize function from velocity module. 
"""

import sys
sys.path.append('../env')
from velocity import Velocity


def custom_or_default_data(dimension, init_velocity, accel=False):
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
            
        except Exception as e:
            print('Info for developer'.upper())
            print(e)
    
    try:
        init_data = Velocity.initialize(dimension=dimension, 
                                        init_velocity=init_velocity, 
                                        accel=accel, 
                                        mock=mock)
    
    except Exception as e:
        print('Info for developer'.upper())
        print(e)
    
    return init_data