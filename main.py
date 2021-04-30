from console.console import Console as console
from application.invoke import Invoke as invoke

if __name__ == '__main__': 
    print()
    print('Welcome to SDC console!')

    while(1):
        module, mode = console.get_command()
        
        if module == 'gps': 
            invoke.gps(mode=mode)
        elif module == 'imu': 
            invoke.imu(mode=mode)
        elif module == 'fuzzy': 
            invoke.fuzzy()
