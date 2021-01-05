import sys, traceback
sys.path.append('../env')
from velocity import Velocity


def custom_or_default_data(dimension, init_velocity, mode, is_accel=False):
    """
    Ask user if parameters should be default. 
    
    Then invoke velocity module `Velocity`. 
    """
    print(f'{dimension}-dimensional space'.upper())

    while(True):
        is_default = input('Default parameters (yes or no)? ')

        try:
            if is_default == 'y' or is_default == 'yes': 
                is_mock = True
                break
            
            elif is_default == 'n' or is_default == 'no':
                is_mock = False
                break
            
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
    
    try:
        init_data = Velocity.initialize(dimension=dimension, 
                                        init_velocity=init_velocity, 
                                        mode=mode,
                                        is_accel=is_accel, 
                                        is_mock=is_mock)
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)
        init_data = None
    
    return init_data