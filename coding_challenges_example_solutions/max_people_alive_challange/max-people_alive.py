## Code to get year w/ max people alive
# by Mark Broich inspired by Gayle Laakmann McDowell's utube video on cracking the coding interview: 
# https://www.youtube.com/watch?v=4UWDyJq8jZg 

# Task: write an algo that return the year with the maximum number of people alive. 

# Make a great example:
# That has many entires, should not be sorted, should have overlapping and non overlapping items
# most people should not be alive at same time; have duplicate years
# should have birth and death in same year

#                    [y_b, y_d]
birth_death_list = [[2000, 2010],
                    [1975, 2005],
                    [1975, 2003],
                    [1803, 1809],
                    [1750, 1869],
                    [1840, 1935],
                    [1803, 1921],
                    [1894, 1921]]

# to test with a large random example
# import random
# birth_death_list = []
# for x in range(1000000):
#     b = random.randint(1900,2020)
#     d = b + random.randint(0,99)
#     birth_death_list.append([b, d])

# start with describing a brute force algo and its big O with y = years and p is persons
# O(y * p) 

# only describe but do not code the brute force function
# coded here to timing comparison and reference  

def brute_force(birth_death_list):
    # get the first birth and last death year in the list
    first_birth = 99999
    last_death = 0
    for person in birth_death_list: 
        y_b = person[0]; y_d = person[1]
        if(y_b < first_birth): first_birth = y_b
        if(y_b > last_death): last_death = y_d
    #
    print(""); print("brute_force number of years to loop over: "+str(len(range(first_birth, last_death+1))))
    print("compare with delta length in other algos")
    #
    max_alive = 0
    year_max_alive = 0
    for year in range(first_birth, last_death+1):
        alive_count = 0
        for person in birth_death_list:
            y_b = person[0]; y_d = person[1]
            # if the person was born and did not yet pass away
            if( (int(y_b) <= year) and (year <= int(y_d)) ):
                alive_count += 1
        if(max_alive < alive_count):
            max_alive = alive_count
            year_max_alive = year
        #
    return year_max_alive

    
# Qs one could ask the interviewer:
# when is an event recorded?
# what is there is a tie? (here assumed to not matter)
# are there negative years?
# are there people that are still alive? 


# Contemplate alogs with better big O: 
# only need to look at time between first and last birth year
# only need to look at unique event years between first and last birth year
# can get algo to O(persons + unique years) by tracking deltas and get max running sum

# Discuss big O
# Be carefull deriving big O (walk through the derivation)
# to get min and max birth year: p
# to to create the min to max birth year array: y
# populate the delta array: p
# to get the max running sum: y
# hence: O(p + y + p + y) so O(p + y)
# possibly mention not just big O of time but also big O of space


# Mentally walk thorugh the code before coding

# Modulearizaition gets one to focus on most interesing part of code and allows testing (testing can be indicated for bonus points)
# One should not code simple functions (ask if one should code the simple functions such as 'get_min_max_birth' rather than start coding
#
def get_pop_peak(birth_death_list):
    if(birth_death_list == ""): # simple test: if empty entry
        return('errorcode')
    #
    # get the first and last birth year
    first_birth, last_birth = get_min_max_birth(birth_death_list) # e.g. 2000 and 2001
    # 
    # make a delta list for addition and removal of a person for each event
    deltas = get_delta(birth_death_list, first_birth, last_birth)
    #
    # get the index of the year when the population is max 
    peak_year_offset = get_max_index_running_sum(deltas)
    #
    return peak_year_offset + first_birth

def get_min_max_birth(birth_death_list):
    first_birth = 99999
    last_birth = 0
    for person in birth_death_list: 
        y_b = person[0]; 
        if(y_b < first_birth): first_birth = y_b
        if(y_b > last_birth): last_birth = y_b
    return first_birth, last_birth

def get_delta(birth_death_list, first_birth, last_birth):
    #init list as long as the number of items between the first and last birth year
    deltas = [0] * (len(range(first_birth,last_birth))+1) # init to zero
    print(""); print('get_pop_peak length detlas_list: '+str(len(deltas)))
    #
    for person in birth_death_list: 
        y_b = person[0]; y_d = person[1] 
        deltas = addDelta(deltas, y_b - first_birth, 1) # increment at index
        if(y_d < last_birth):
            deltas = addDelta(deltas, y_d - first_birth + 1, -1) # decrement at year after death index
    return deltas

def addDelta(deltas, y_event, increment):
    deltas[y_event] = deltas[y_event] + increment
    return deltas

def get_max_index_running_sum(deltas):
    running_sum = 0
    max_running_sum = 0
    year_peak = 0
    for year in range(0, len(deltas)):
        running_sum += deltas[year]
        if(running_sum > max_running_sum):
            max_running_sum = running_sum
            year_peak = year
    return year_peak


# NOW TEST THE CODE!
# First walk through the logic; Do not just look at the final output
# Then walk through with an tiny example
# Look for trouble spots (e.g. off by one error, math, do parameters match, what if loop does not operate?
# Check math with small values close together (e.g. first_birth = 2000 last_birth = 2000 but need two slots to increment so last_birth - first_birth + 1)
# When finding a bug think about the cause and fix rather than the first fix that comes to mind
# Going through with a simple case helps catch small but common bugs that may be lurking
# Only then go through with full example and test edge cases


# Get py libs for timing and sci notification runtime comparison
import time
from decimal import Decimal

# Run and time the brute_force
t0 = time.time()
year_max_alive = brute_force(birth_death_list)
print("brute_force result: "); print("year max alive: "+str(year_max_alive))
t1 = time.time()
runtime_O_of_P_times_Y_algo = t1-t0


# Run and time the runtime_O_of_P_plus_Y_algo  
t0 = time.time()
year_max_alive = get_pop_peak(birth_death_list)
print("get_pop_peak result: "); print("year max alive: "+str(year_max_alive))
t1 = time.time()
runtime_O_of_P_plus_Y_algo = t1-t0


#### For bonus points: 
# Make runtime_O_of_P_plus_Y_algo even faster by considering only unique event years between first and last birth year
def get_pop_peak_faster(birth_death_list):
    if(birth_death_list == ""): # simple test: if empty entry
        return('errorcode')
    #
    # get the first and last birth year
    first_birth, last_birth = get_min_max_birth(birth_death_list) # e.g. 2000 and 2001
    #
    # get_unique_sorted_event_years !! 
    unique_sorted_event_years = get_unique_sorted_event_years(birth_death_list,first_birth,last_birth)
    #
    # make a delta list for addition and removal of a person for each event
    deltas = get_delta_fewer(birth_death_list, unique_sorted_event_years, first_birth, last_birth)
    #
    # get the index of the year when the population is max 
    peak_year_offset = get_max_index_running_sum(deltas)
    #
    return unique_sorted_event_years[peak_year_offset]

def get_unique_sorted_event_years(birth_death_list,first_birth,last_birth):
    unique_event_years = set()
    for person in birth_death_list: 
        y_b = person[0]; y_d = person[1]; 
        if(y_b <= last_birth): unique_event_years.add(y_b)
        if(y_d < last_birth): unique_event_years.add(y_d)
    return sorted(unique_event_years)

def get_delta_fewer(birth_death_list, unique_sorted_event_years, first_birth, last_birth):
    # init list as long as the number of unique items between the first and last birth year
    deltas = [0] * len(unique_sorted_event_years) # init to zero
    print(""); print('get_pop_peak_faster length detlas_list: '+str(len(deltas)))
    #
    for person in birth_death_list: 
        y_b = person[0]; y_d = person[1] 
        # work out where in the unique_sorted_event_years the event needs to increment or decrement
        index_y_b = unique_sorted_event_years.index(y_b)
        deltas = addDelta(deltas, index_y_b, 1) 
        if(y_d < last_birth):
            index_y_d = unique_sorted_event_years.index(y_d)
            deltas = addDelta(deltas, index_y_d +1, -1) # decrement year after death
    return deltas


# Time the get_pop_peak_faster algo
t0 = time.time()
year_max_alive = get_pop_peak_faster(birth_death_list)
print("get_pop_peak_faster result: "); print("year max alive: "+str(year_max_alive))
t1 = time.time()
runtime_O_of_P_plus_Y_algo_faster = t1-t0


# Compare the runtimes by deviding the Gayle Laakmann McDowell-inspired algo's runtime by the brute_forth algo runtime
percent_time =  round(runtime_O_of_P_plus_Y_algo / runtime_O_of_P_times_Y_algo * 100, 2)
print("my py implementation of Gayle Laakmann McDowell algo runs in "+str(percent_time)+"% that my brute force algo took"); print("")

# Compare runtimes in sci notation
print('runtime_O_of_P_times_Y_algo        '+'%.2E' % Decimal(runtime_O_of_P_times_Y_algo))
print('runtime_O_of_P_plus_Y_algo         '+'%.2E' % Decimal(runtime_O_of_P_plus_Y_algo))
print('runtime_O_of_P_plus_Y_algo_faster  '+'%.2E' % Decimal(runtime_O_of_P_plus_Y_algo_faster))




### Older version of the brute force algo that does a bunch of unnecessary stuff such as dealing with 
# people still alive and returning the number of people alive during the max alive year
def brute_force_w_extra(person_birth_death_list, first_birth, last_death):
    max_alive = 0
    year_max_alive = 0
    # number of years to loop over
    print(""); print("number of years to loop over: "+str(len(range(first_birth, last_death+1))))
    print("compare with delta length")
    #
    for year in range(first_birth, last_death+1):
        alive_count = 0
        for person in person_birth_death_list:
            name, b_y, d_y = person.split(", ")
            # if the person was born and is still alive
            if( (int(b_y) <= year) and ( ('alive' == d_y) or (year <= int(d_y)) ) ):
                alive_count += 1
        if(max_alive < alive_count):
            max_alive = alive_count
            year_max_alive = year
    print("year max alive: "+str(year_max_alive)+" number alive: "+str(max_alive))

person_birth_death_list = ['a, 2000, 2010' ,'b , 1975, 2005' , 'c, 1975, 2003' , 'd, 1803, 1809' , 'e, 1750, 1869' , 'f, 1840, 1935' , 'g, 1803, 1921' , 'h, 1894, 1921']
first_birth = 1750
last_death = 2010

brute_force_w_extra(person_birth_death_list, first_birth, last_death)


## output example:
# brute_force number of years to loop over: 261
# compare with delta length in other algos
# brute_force result: 
# year max alive: 1803

# get_pop_peak length detlas_list: 251
# get_pop_peak result: 
# year max alive: 1803

# get_pop_peak_faster length detlas_list: 10
# get_pop_peak_faster result: 
# year max alive: 1803
# my py implementation of Gayle Laakmann McDowell algo runs in 8.56% that my brute force algo took

# runtime_O_of_P_times_Y_algo        4.90E-04
# runtime_O_of_P_plus_Y_algo         4.20E-05
# runtime_O_of_P_plus_Y_algo_faster  2.48E-05

# number of years to loop over: 261
# compare with delta length
# year max alive: 1803 number alive: 3
