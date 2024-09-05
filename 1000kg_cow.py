#this is a 1000kg cow

import numpy as np
import matplotlib as plt

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
    grav          = 9.8 	#m/s^2
    init_pos_cow  = [0,100] 
    init_vel_cow  = [10,10]
    wind_res_cons = 0.01
    time	  = 0.0
    dt            = 0.1

    position = np.array(init_pos_cow)
    velocity = np.array(init_vel_cow)
    
    while position[1] > 0.0:
 	
 	f_tot = tot_force_vec(velocity,mass,g,wind_res_cons)
 	velocity, position = curr_pos_vel_calc(position,velocity,f_tot,mass,dt)
 	eng_kinetic, eng_poten, eng_tot = eng_calculator(position,velocity,mass,g)
 		
 	pos_list.append(position)
 	vel_list.append(velocity)
 	eng_list.append(eng_tot)
 	time_list.append(time)
 		
 	time += dt
 	return np.array(time_list), np.array(pos_list), np.array(vel_list), np.array(eng_list)
##-----------------------------------------------------------------------##
test_function()
##-----------------------------------------------------------------------##

#input:
#   pos_cow = a list with the x and y coordinates of the cow
#   vel_cow = a list with the Vx and Vy velocities of the cow
#output
#   tot_force_vec = a list with the force of 
def calc_total_force(pos_cow, vel_cow)
    tot_force_vec = [0,0]
    return tot_force_vec

