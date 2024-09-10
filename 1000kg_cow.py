#this is a 1000kg cow

import numpy as np
import matplotlib.pyplot as plt

##-----------------------------------------------------------------##
def eng_calculator(position,velocity,mass,g):
    #KE=0.5*m*v^2
    eng_kinetic = 0.5 * mass * np.sum(velocity**2)
    
    #PE=m*g*h
    eng_poten = mass * g * position[1]
    
    #E=KE+PE
    eng_tot = eng_kinetic + eng_poten
    
    return eng_kinetic, eng_poten, eng_tot
##-----------------------------------------------------------------##
def curr_pos_vel_calc(position,velocity,f_tot,mass,dt):
    #f=ma
    accel = f_tot / mass
    
    #v=v0+adt
    curr_vel = velocity + (accel * dt)
    
    #r=r0+vdt
    curr_pos = position + (velocity * dt)
    
    return curr_vel, curr_pos
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
    mass          = 1000 	#kg
    g             = 9.8 	#m/s^2
    init_pos_cow  = [0,100] 
    init_vel_cow  = [10,10]
    wind_res_cons = 1.0
    time	  = 0.0
    dt            = 0.01

    position = np.array(init_pos_cow)
    velocity = np.array(init_vel_cow)
    
    time_list   = []
    pos_x_list  = []
    pos_y_list  = []
    vel_x_list  = []
    vel_y_list  = []
    eng_tot_x_list = []
    eng_tot_y_list = []
    eng_kinetic_x_list = []
    eng_kinetic_y_list = []
    eng_poten_x_list = []
    eng_poten_Y_list = []
    
    while position[1] > 0.0:
 	
 	    f_tot = tot_force_vec(velocity,mass,g,wind_res_cons)
 	    velocity, position = curr_pos_vel_calc(position,velocity,f_tot,mass,dt)
 	    eng_kinetic, eng_poten, eng_tot = eng_calculator(position,velocity,mass,g)
 	    
 	    #print(time, '\t',position,'\t', velocity,'\t', eng_kinetic,'\t', eng_poten,'\t', eng_tot,'\n')
 	    	
 	    pos_x_list.append(position[0])
 	    pos_y_list.append(position[1])
 	    vel_x_list.append(velocity[0])
 	    vel_y_list.append(velocity[1])
 	    eng_tot_x_list.append(eng_tot[0])
 	    eng_tot_x_list.append(eng_tot[1])
 	    eng_kinetic_x_list.append(eng_kinetic[0])
 	    eng_kinetic_y_list.append(eng_kinetic[1])
 	    eng_poten_x_list.append(eng_poten[0])
 	    eng_poten_y_list.append(eng_poten[1])
 	    
 	    time_list.append(time)
 	    
 	    time += dt
    #return np.array(time_list), np.array(pos_list), np.array(vel_list), np.array(eng_list)
  
    plt.figure()
    plt.plot(pos_x_list, pos_y_list)
    plt.show()
    	
    	
##-----------------------------------------------------------------------##
def display_lists(data_arr):

    print("Time(s)  Position(x,y) Velocity(Vx,Vy) Energy(KE, PE, TE) ")

##-----------------------------------------------------------------------##
def getTrajectFile(time_list, x_list, y_list)
    file = open("KMS_Trajectory.txt", 'w')
    file.write("Time   X    Y")
    for i in length(time_list)
        file.write(time_list[i],"\t", x_list[i], "\t", y_list[i], "\n")

##-----------------------------------------------------------------------##
test_function()
##-----------------------------------------------------------------------##

