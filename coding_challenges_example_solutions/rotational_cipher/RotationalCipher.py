# Rotational Cipher

# One simple way to encrypt a string is to "rotate" every alphanumeric 
# character by a certain amount. Rotating a character means replacing 
# it with another character that is a certain number of steps away in 
# normal alphabetic or numerical order.

# For example, if the string "Zebra-493?" is rotated 3 places, the 
# resulting string is "Cheud-726?". Every alphabetic character is 
# replaced with the character 3 letters higher (wrapping around 
# from Z to A), and every numeric character replaced with the 
# character 3 digits higher (wrapping around from 9 to 0). 
# Note that the non-alphanumeric characters remain unchanged.
# Given a string and a rotation factor, return an encrypted string.

# Ot(n) and Os(n)

# am using 3 dict: charPosDict, PosCharDict
# and numDict 
# I use charPosDict to get the index of a character
# and PosCharDict to get the letter of index + shift
# 
def rotationalCipher(input, rotation_factor): 
  if rotation_factor == 0:
      return input
  output = ""  
  for i in range(len(input)):  
      if input[i] in charPosDict:
        j, cap = charPosDict[input[i]]
        j += rotation_factor
        if j > len(charPosDict)/2:  
          # account for warp around                
          j = j % int(len(charPosDict)/2)       
        indexTuple = (j,cap)         
        output += PosCharDict[indexTuple]
      elif input[i] in numDict:
        j = numDict[input[i]] 
        j += rotation_factor  
        if j > len(numDict)-1:
          # account for warp around           
          j = j % len(numDict)
        output  += str(j)
      else:
        output += input[i]
  return output 

# I could also use inbuilt functions such as: 
# chr(ord('i')+1)
# returns index: 
# ord('i')+1


# dict where key is a letter and the value is 
# a tuple of the letter's index and if it is a 
# capital or not
charPosDict = {'a':(1,0),'A':(1,1),
                 'b':(2,0),'B':(2,1),
                'c':(3,0),'C':(3,1),
                'd':(4,0),'D':(4,1),
                'e':(5,0),'E':(5,1),
                'f':(6,0),'F':(6,1),
                'g':(7,0),'G':(7,1),
                'h':(8,0),'H':(8,1),
                'i':(9,0),'I':(9,1),
                'j':(10,0),'J':(10,1),
                'k':(11,0),'K':(11,1),
                'l':(12,0),'L':(12,1),
                'm':(13,0),'M':(13,1),
                'n':(14,0),'N':(14,1),
                'o':(15,0),'O':(15,1),
                'p':(16,0),'P':(16,1),
                'q':(17,0),'Q':(17,1),
                'r':(18,0),'R':(18,1),
                's':(19,0),'S':(19,1),
                't':(20,0),'T':(20,1),
                'u':(21,0),'U':(21,1),
                'v':(22,0),'V':(22,1),
                'w':(23,0),'W':(23,1),
                'x':(24,0),'X':(24,1),
                'y':(25,0),'Y':(25,1),
                'z':(26,0),'Z':(26,1)}
  
# dict where key is a tuple of letter index 
# and if it is a capital or not 
# the value is the letter
PosCharDict = {(1,0):'a', (1,1):'A',
                 (2,0):'b', (2,1):'B',
                 (3,0):'c', (3,1):'C',
                 (4,0):'d', (4,1):'D',
                 (5,0):'e', (5,1):'E',
                 (6,0):'f', (6,1):'F',
                 (7,0):'g', (7,1):'G',
                 (8,0):'h', (8,1):'H',
                 (9,0):'i', (9,1):'I',
                 (10,0):'j', (10,1):'J',
                 (11,0):'k', (11,1):'K',
                 (12,0):'l', (12,1):'L',
                 (13,0):'m', (13,1):'M',
                 (14,0):'n', (14,1):'N',
                 (15,0):'o', (15,1):'O',
                 (16,0):'p', (16,1):'P',
                 (17,0):'q', (17,1):'Q',
                 (18,0):'r', (18,1):'R',
                 (19,0):'s', (19,1):'S',
                 (20,0):'t', (20,1):'T',
                 (21,0):'u', (21,1):'U',
                 (22,0):'v', (22,1):'V',
                 (23,0):'w', (23,1):'W',
                 (24,0):'x', (24,1):'X',
                 (25,0):'y', (25,1):'Y',
                 (26,0):'z', (26,1):'Z',
                }

# number dict where the key is a str and the value the number  
numDict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_case_number = 1

  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)


