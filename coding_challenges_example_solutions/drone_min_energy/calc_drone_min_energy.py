'''
Drone Flight Planner

You’re an engineer at a disruptive drone delivery startup and your CTO asks
you to come up with an efficient algorithm that calculates the minimum amount
of energy required for the company’s drone to complete its flight. You know
that the drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile
it ascends, and it gains 1 kWh for every mile it descends. Flying sideways
neither burns nor adds any energy.

Given an array route of 3D points, implement a function calcDroneMinEnergy
that computes and returns the minimal amount of energy the drone would need
to complete its route. Assume that the drone starts its flight at the first
point in route. That is, no energy was expended to place the drone at the
starting point.

For simplicity, every 3D point will be represented as an integer array whose
length is 3. Also, the values at indexes 0, 1, and 2 represent the x, y 
and z coordinates in a 3D point, respectively.

Explain your solution and analyze its time and space complexities.

Example:

input:  route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than `5` kWh and it’d end up with excess energy

Constraints:
[time limit] 5000ms
[input] array.array.integer route
1 ≤ route.length ≤ 100
[output] integer
'''

'''
Approach: if we take off without fuel, we will have the largest
negative fuel in the tank when we reach the max height
(from there on we do not need any more fuel to compelte the flight).
So, init fule to zero, track min tank and return min tank * -1
unless min tank is a positive, which happends if w start at max height.
'''

# Ot(n)
# O(1)
def calc_drone_min_energy(route):
  if len(route) <= 1:
    return 0
  fuel = 0
  minFuel = float('inf')

  for i in range(0, len(route) -1):
      fuel += route[i][2] - route[i+1][2]
      minFuel = min(fuel, minFuel)
  if minFuel >= 0:
    return 0
  return minFuel * -1
