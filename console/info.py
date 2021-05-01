class Info: 
    """
    Allows to print out information about the application. 
    """
    
    def commands():
        print('''Main modules:
    imu             | Inertial Measurement Unit (GPS, gyro, accelerometer)
    gps             | GPS 
    gyro            | Gyroscope 
    accel           | Accelerometer
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
