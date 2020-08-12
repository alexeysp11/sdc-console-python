# Fuzzy controller takes dstnce2prev_pt and dstnce2nxt_pt as the input varibles
# and returns two values of speed as the output variables
# One of them is defined by dstnce2prev_pt, another one is defined by dstnce2nxt_pt
# First output variable might be called as speed_prev_pt, the second one as speed_nxt_pt


# LIBRARIES
import fuzzy_controller
import matplotlib.pyplot as plt


# FUZZY CONTROLLER TESTING CLASS
class TestFuzzyController:
    
    # SHOW LINGUISTIC VARIABLES METHOD
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


    # RELATIONSHIP BETWEEN DISTANCE AND SPEED
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


    # TRANSFER DISTANCE TO SPEED 
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


    # WRITE DISTANCE AND GET SPEED 
    def get_distance_set_speed(self, fc):
        # get a distance 
        distance = input('Distance (m): ')

        # EXCEPTIONS HANDLING
        # try this 
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


# MAIN FUNCTION 
def main():
    # Declare instances of considered classes
    fc = fuzzy_controller.FuzzyController()
    fc_test = TestFuzzyController()
    
    # If you need to enter distance and get speed, run this function:
    get_set = fc_test.get_distance_set_speed(fc)
    print(get_set)
    
    # If you need to describe the relationship between distance and speed
    # in the graph, run this fuction: 
##    rel_dstnce_speed(fuzzy_controller)


if __name__ == '__main__':
    main()
