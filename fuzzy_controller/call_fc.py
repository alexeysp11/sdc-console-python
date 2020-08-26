import fuzzy_controller
import matplotlib.pyplot as plt


class CallFuzzy:
    def call(self):
        # Declare instances of considered classes
        fc = fuzzy_controller.FuzzyController()
        self = CallFuzzy()
        
        # If you need to enter distance and get speed, run this function:
        get_set = self.get_distance_set_speed(fc)
        print(get_set)
        
        """
        If you need to describe the relationship between distance and speed
        in the graph, run this fuction: 
        """
    ##    self.rel_dstnce_speed(fuzzy_controller)
    
    
    def view_variables(self, fc, entered_distance):
        # show linguistic variables' domain
        # MAKE ALL GRAPHS IN ONE WINDOW! 
        fc.distance.view()
        fc.speed.view()

        # get speed 
        speed = fc.count_speed(entered_distance)
        # plot 
##        self.view_variables(distance)

        # view linguistic variables and counted values of distance and speed
        fc.distance.view(sim=self.speed_simulation)
        fc.speed.view(sim=self.speed_simulation)


    # Relationship between distance and speed
    def draw_plot(self, speed_axis, distance_axis):
        # plotting the points
        plt.plot(speed_axis, distance_axis)
        
        # naming the x axis and the y axis
        plt.xlabel('Speed (km/h')
        plt.ylabel('Distance (m)')
        
        # giving a title to my graph 
        plt.title('Relationship between distance and speed')
        
        # function to show the plot 
        plt.show() 


    # Transfer distance to speed 
    def rel_dstnce_speed(self):
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
        draw_plot(array_speed, array_distance)


    # Write distance and get speed 
    def get_distance_set_speed(self, fc):
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
            return 'Speed = ' + str(speed) + ' km/h'
