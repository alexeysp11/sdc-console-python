import fuzzy_controller
import matplotlib.pyplot as plt


class CallFuzzy:
    """
    This class allows you to configure interaction with `FuzzyController` class 
    from the console application. 
    
    `FuzzyController` is tend to be  the saperate part of the program, 
    so you can reuse `FuzzyController` class in the similar program (for example, 
    if you modelling some movements of a car). 
    """
    def call(self):
        """
        Call `FuzzyController` from the console application.
        """

        # Declare instances of considered classes
        fc = fuzzy_controller.FuzzyController()
        self = CallFuzzy()
        
        print("""Select one of these options:
            1) Enter distance and get speed once, 
            2) Describe relationship between distance and speed in the graph.
            """)

        while(True):
            command = input('Please, enter 1 or 2: ')

            if command == '1':
                # If you need to enter distance and get speed, run this function:
                distance, speed = self.get_distance_set_speed(fc)
                
                # show linguistic variables. 
                self.view_variables(fc, distance)

                # print out entered speed. 
                print(f'Speed = {speed} km/h')
                
                break
            
            elif command == '2':
                """
                If you need to describe the relationship between distance and speed
                in the graph, run this fuction: 
                """

                # show linguistic variables. 
                #self.view_variables(fc)

                self.rel_dstnce_speed(fc)
                break


    def view_variables(self, fc, entered_distance=None):
        """
        Show linguistic variables' domain (`distance` as an input and `speed` as 
        an output). 
        """
        fc.distance.view()
        fc.speed.view()

        if entered_distance != None:
            # get speed 
            speed = fc.count_speed(entered_distance)
            
            # plot 
            #self.view_variables(distance)

            # view linguistic variables and counted values of distance and speed
            fc.distance.view(sim=fc.speed_simulation)
            fc.speed.view(sim=fc.speed_simulation)


    def draw_plot(self, speed_axis, distance_axis):
        """
        Draw an initial relationship between `distance` and `speed` initiated in 
        the rulebase of `FuzzyController` class. 
        """
        # plotting the points
        plt.plot(distance_axis, speed_axis)
        
        # naming the x axis and the y axis
        plt.xlabel('Distance (m)')
        plt.ylabel('Speed (km/h')
        
        # giving a title to my graph 
        plt.title('Relationship between distance and speed')
        
        # function to show the plot 
        plt.show() 


    def rel_dstnce_speed(self, fuzzy_controller):
        """
        Print out and plot the relationship between `distance` and `speed` 
        initiated in the rulebase. 

        Plot a diagram of the relationship by calling `draw_plot()` method. 
        """
        distance = 0
        max_distance = 100
        step = 1.25
        
        # Declare empty lists named array_distance and array_speed
        array_distance = []
        array_speed = []
        i = 0
        number_of_elements = int(max_distance / step)
        
        # Create arrays 
        for i in range(number_of_elements + 1):
            speed = fuzzy_controller.count_speed(distance)
            array_distance.append(distance)
            array_speed.append(speed)
            i += 1
            distance = distance + step
        
        # Print out a table of distance and speed
        print('Distance (m)\tSpeed (km/h)')
        i = 0 
        for i in range(number_of_elements + 1):
            print(str(array_distance[i]) + '\t\t' + str(array_speed[i]))
        
        self.draw_plot(array_speed, array_distance)


    def get_distance_set_speed(self, fc):
        """
        This method allows you to write value of `distance` in the console and 
        get value of `speed` corresponding to the `distance`. 

        Variable `distance` is measured in meters, and `speed` is measured 
        in km/h.

        :returns: floating point `distance`, floating point `speed`.
        """

        # get a distance 
        distance = input('Distance (m): ')

        try:
            # convert input distance into float number
            distance = float(distance)
            
            # if distance is negative throw an exception
            if distance < 0:
                return 'Distance is negative'
            
        # if user passed a string 
        except Exception:
            return 'Incorrect input'
        
        # if there's no exceptions 
        else:
            # count a speed with the help of fuzzy controller 
            speed = fc.count_speed(distance)
            return float(distance), float(speed)
