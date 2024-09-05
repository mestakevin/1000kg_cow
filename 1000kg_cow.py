#this is a 1000kg cow

import numpy as np
import matplotlib as plt


##-----------------------------------------------------------------##
def tot_force_vec(velocity,mass,g,wind_res_cons):
    f_grav = -mass * g
    
    v_magnitude = np.sqrt(velocity[0]**2 + velocity[1]**2)
    
    f_wind_x = -wind_res_cons * velocity[0] * v_magnitude
    f_wind_y = -wind_res_cons * velocity[1] * v_magnitude
    
    f_tot_x = f_wind_x
    f_tot_y = f_grav + f_wind_y
    f_tot   = np.array([f_tot_x,f_tot_y])

    return f_tot
##-----------------------------------------------------------------------##
def test_function():
    #Inital conditions
    mass_cow      = 1000 #kg
    grav          = 9.8 #m/s^2
    init_pos_cow  = [0,100] 
    init_vel_cow  = [10,10]
    wind_res_cons = 0.01
    time	  = 0.0
    dt            = 0.1

    position = np.array(init_pos_cow)
    velocity = np.array(init_vel_cow)
##-----------------------------------------------------------------------##



