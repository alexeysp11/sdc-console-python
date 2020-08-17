"""
Info
"""

def info():
    print('''Information:
    imu         | inertial measurement unit ()
    gps         | gps (non-constant velocity)
    position    | gps (constant velocity) 
    accel       | gps (acceleration)
    gyro        | gyroscope
    lidar       | lidar
    fuzzy       | fuzzy controller 
    nn mnist    | neural network (mnist)
    test        | unit tests for each module
    exit        | exit 
    ''')


def gps(): 
    print('''gps module:
    velocity    | gps (non-constant velocity)
    position    | gps (constant velocity) 
    ''')


def gyro():
    pass
