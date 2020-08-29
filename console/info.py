"""
Information module
"""

def commands():
    print('''Main modules:
    imu             | Inertial Measurement Unit (GPS, gyro, accelerometer)
    gps             | GPS 
    gyro            | Gyroscope 
    accel           | Accelerometer
    lidar           | Lidar
    fuzzy           | Fuzzy Controller 
    nn              | Neural Network 
    test            | Unit-tests for each module
    exit            | Exit 
    ''')


def help():
    print('''SDC CONSOLE APP

SDC stands for Self-Driving Cars. 
So this app allows you to simulate some modules of SDC within a console.

All modules can be called by:
    sdc module --mode

All information modules can be called by:
    sdc -commands
    sdc -help
    ''')


def imu(): 
    print('''sdc imu:
    --p             | IMU (position) 
    --v             | IMU (velocity)
    --a             | IMU (acceleration)
    ''')


def gps(): 
    print('''sdc gps:
    --p             | GPS (position) 
    --v             | GPS (velocity)
    --a             | GPS (acceleration)
    ''')


def gyro():
    print('''sdc gyro:
    --const         | Gyroscope (constant angle)
    --nu            | Gyroscope (non-uniform rotation) 
    ''')


def neural_network():
    print("""sdc nn:
    --minst default | MNIST dataset of digits (default)
    --minst custom  | MNIST dataset of digits (custom)
    --signs         | Road signs
    """)
