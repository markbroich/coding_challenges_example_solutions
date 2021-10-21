'''
Given avaible tile slots of A and B and
a duration 
return the first avaiable time slot where 
both A and B can meet for duration dur
'''

# Ot(m+n) 
# Os(1)

def meeting_planner(slotsA, slotsB, dur):
  if len(slotsA) == 0 or len(slotsB) == 0:
    return []
  a = b = 0
  out= []
  while a < len(slotsA) and b < len(slotsB): ###
    overSt = max(slotsA[a][0], slotsB[b][0])
    overEn = min(slotsA[a][1], slotsB[b][1])
    if overEn - overSt >= dur:
      out = [overSt, overSt+dur]
      return out
    elif slotsA[a][1] < slotsB[b][1]:
      a += 1
    else:
      b += 1
  return out


# ex1
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
exp = [60, 68]
print(meeting_planner(slotsA, slotsB, dur) == exp)

# ex2
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 12
exp = []
print(meeting_planner(slotsA, slotsB, dur) == exp)