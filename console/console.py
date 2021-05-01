import os 
import sys                          # for exit. 
from .info import Info as info      # for Info class. 

class Console: 
    """
    Gets data that user inputs into console. 
    """

    def get_command():
        """
        Gets commands that user inputs into console. 

        Returns: 

        `module`: what module should be invoked (GPS, IMU, fuzzy controller etc). 

        `mode`: mode of a module (for example, constant speed, random 
        acceleration etc).
        For some modules (like fuzzy controller) there is no mode parameter, 
        so just return `mode` equal to something like `'0'`. 
        """

        while True:
            try:
                command = input('>> ')
                
                # ignore if user just pressed Enter
                if command == '':
                    pass
                
                elif command == 'sdc':
                    info.help()
                    info.commands()

                elif command == 'sdc -commands':
                    info.commands()
                
                elif command == 'sdc -h' or command == 'sdc -help':
                    info.help()
                
                elif command == 'sdc imu':
                    info.imu()
                
                elif command == 'sdc imu --p':
                    return 'imu', 'p'

                elif command == 'sdc imu --v':
                    return 'imu', 'v'
                
                elif command == 'sdc imu --a':
                    return 'imu', 'a'

                elif command == 'sdc gps':
                    info.gps()

                elif command == 'sdc gps --p':
                    return 'gps', 'p'

                elif command == 'sdc gps --v':
                    return 'gps', 'v'
                    invoke.gps(mode='v')
                
                elif command == 'sdc gps --a':
                    return 'gps', 'a'
                
                elif command == 'sdc fuzzy':
                    return 'fuzzy', '0'

                elif command == 'sdc exit':
                    sys.exit()
                
                else:
                    print('Incorrect command!')
            
            except Exception as e:
                print('Info for developer:'.upper)
                print(e)


    def is_default(dimension):
        """
        Asks user if parameters should be default. 
        
        Returns: 

        `True` if data should be default. 

        `False` if data should not be default. 
        """

        print(f'{dimension}-dimensional space'.upper())

        while(True):
            is_default = input('Default parameters? ')

            try:
                if is_default == 'y' or is_default == 'yes': 
                    return True
                
                elif is_default == 'n' or is_default == 'no':
                    return False
                
            except Exception as e:
                print('Exception: '.upper(), e)
                traceback.print_tb(e.__traceback__)
        
        return init_data
