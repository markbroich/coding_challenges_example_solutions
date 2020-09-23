## SCENARIO: 
# A car may be won doing a game show. 
# The show has x closed doors with one door hiding a price (a sports car) 
# and all other doors hiding goats (losses)

# the player choses a door. The host will open all but one other doors that the player did not chose revealing goats (losses). 
# e.g. if there are 5 doors and the player picks door #1, the host may open door 2,3,4 revealing goats (losses). 
# THe player is then asked to either stick with the door initially chosen or to switch to the only other closed doors that is remaining 
# with the aim of winning the price.   

# one may think that staying with the door initially chosen or switching to the only other door the host 
# did not open has an equal (1/2) chance of winning the car.
# but not so fast! 

# lets simulate for x doors (the original game show had 3 doors) and compare the number of times the player would win when staying vs switching

from random import randint

def monty_sim(door_count, stay=False):
    correct_door_chosen = randint(1,door_count) == 1 # assuming door 1 is chosen
    if stay:
        return correct_door_chosen
    else: 
        return not correct_door_chosen

runs = 10000
won_stay = 0
won_switch = 0
door_count = 30
for i in range(0,runs):
    won_stay += (monty_sim(door_count, stay = True))
    won_switch += (monty_sim(door_count, stay = False))

print("")
print("results of: ", runs, " simulation runs: ")
print('won when staying fraction: ', round(won_stay/runs,4))
print('won when switching fraction: ', round(won_switch/runs,4))
print('times a likely to win when switching: ', round((won_switch/runs) / (won_stay/runs),2),"\n")



# Ok, and here is the calculation of probability explaining the simulated result

# via equation: conditional probability:
# P(A|B) = probability of A given B
# A is players 
# B is the host having opened all doors except the players initial choice and one other
# B is the chance of a specific door (out of the once that the player did not pick) remains closed 
# (after the host opens all other doors). 

# p of winning when staying with the door (that was correct all along)
# if the player picks the correct door door not opened by the host is chosen with a 1/(door_count-1) probability given 
# that the host can keep any door closed other than the once chosen by the player, which remains closed by default. 
p_correct_door = 1 /door_count * 1 /(door_count-1) 
# p of winning when switching to the only other door not opened (the initial choice was false)
# here B = 1 as the host will have to open all doors not chosen by the player except for the door hiding the price
# this is the probability of the initial door beeing wrong given B OR the probability of winning when switching
p_incorrect_door = 1/door_count * 1 

print("equation result: ")
print("p of winning when staying: ", round(p_correct_door,4))    # should stay
print("p of winning when switching: ", round(p_incorrect_door,4))  # better to swtich
print(p_incorrect_door/p_correct_door, " times a likely to win when switching")
