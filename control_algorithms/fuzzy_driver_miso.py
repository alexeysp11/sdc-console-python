import sys, traceback 

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sys.path.append('../maths')
from maths.fc_miso import FcMiso as FuzzyController


class FuzzyDriverMiso:
    """
    This class allows you to configure interaction with `FuzzyController` class 
    from the console application. 
    """
    def call(self):
        """
        Calls `FuzzyController` from the console application.
        """

        # Declare an instance of `FuzzyController` class
        fc = FuzzyController()

        print("""VARIABLES: 
        In: Distance to next point. 
        In: Distance to previous point. 
        In: Angle.
        Out: Speed.""")
        
        print("""Select one of these options:
            1) Enter input variables and get output variable only once, 
            2) Describe relationship between input and output variable using a graph.
            """)

        while(True):
            command = input('Please, enter 1 or 2: ')
            if command == '1':
                speed = self.get_speed_console(fc)
                print(f'Speed = {speed} km/h') 
                break
            elif command == '2':
                self.relationship(fc)
                break


    def draw_plot(self, input1, input2, input3, output, view):
        """
        Allows to visualize relationship between 3 input variables of fuzzy 
        controller (distance to the previous point `dpp`, distance to 
        the next point `dnp` and angle of rotation `angle` in degrees) 
        and its output variable (speed of a car `speed`). 

        Graph is drawn as 3D plot of 3 input variables, output variable
        is shown using colorbar. 
        """
        if view == 'subplots': 
            pass
        if view == '3d':
            # convert to 2d matrices
            input1, input2 = np.meshgrid(input1, input2)            # 10x10
            input3 = np.outer(input3.T, input3) / np.max(input3)    # 10x10
            output = np.outer(output.T, output) / np.max(output)    # 10x10

            # fourth dimention - colormap
            mappable = plt.cm.ScalarMappable(cmap='seismic')
            mappable.set_array(output)

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(input1, input2, input3, 
                cmap=mappable.cmap, norm=mappable.norm, 
                linewidth=0, antialiased=False)
            fig.colorbar(mappable)
            
            ax.set_xlabel('DPP (m)')
            ax.set_ylabel('DNP (m)')
            ax.set_zlabel('Angle (deg)')
            plt.title('Three variable fuzzy controller')
            plt.grid()
            plt.show() 
        else: 
            raise f'Incorrect parameter of view: {view}'


    def relationship(self, fuzzy_controller):
        """
        Print out and plot the relationship between `distance` and `speed` 
        initiated in the rulebase. 

        Plot a diagram of the relationship by calling `draw_plot()` method. 
        """

        dstnce_prev = np.arange(0.0, 50.0, 5.0)
        dstnce_next = np.arange(0.0, 50.0, 5.0)
        angle = np.arange(-45.0, 45.0, 9.0)
        speed = []
        try: 
            for x in dstnce_prev:
                for y in dstnce_next: 
                    for z in angle: 
                        result = fuzzy_controller.inference(x, y, z)
                        speed.append(result)
                        print(f'x: {x}\ty: {y}\tz: {z}\tresult: {result}')
            speed = np.asarray(speed)
            self.draw_plot(input1=dstnce_prev, input2=dstnce_next, 
                input3=angle, output=speed, view='3d')
        except Exception: 
            pass 


    def get_speed_console(self, fc):
        """
        This method allows you to write value of `distance` in the console and 
        get value of `speed` corresponding to the `distance`. 

        Variable `distance` is measured in meters, and `speed` is measured 
        in km/h.

        :returns: floating point `distance`, floating point `speed`.
        """
        while (1): 
            dstnce_prev = input('Distance to previous point (m): ')
            try:
                dstnce_prev = float(dstnce_prev)
                if dstnce_prev < 0:
                    raise 'Distance cannot be negative'
                else: 
                    break
            except Exception:
                print('Incorrect input')
        
        while (1): 
            dstnce_next = input('Distance to next point (m): ')
            try:
                dstnce_next = float(dstnce_next)
                if dstnce_next < 0:
                    raise 'Distance cannot be negative'
                else:
                    break
            except Exception:
                print('Incorrect input')
        
        while (1):
            angle = input('Angle of rotation (deg): ')
            try:
                angle = float(angle)
                if angle < -90 and angle > 90:
                    raise 'Angle is out of range'
                else: 
                    break
            except Exception:
                print('Incorrect input')
        
        speed = fc.inference(dpp_in=dstnce_prev, 
            dnp_in=dstnce_next, 
            angle_in=angle)
        return float(speed)
