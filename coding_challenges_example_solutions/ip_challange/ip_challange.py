
'''
Validate IP Address

Validate an IP address (IPv4). 
An address is valid if and only if it is in the form "X.X.X.X", 
where each X is a number from 0 to 255.

For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" 
are valid IP addresses, while "12.34.56.oops", "1.2.3.4.5", 
and "123.235.153.425" are invalid IP addresses.

Examples:

ip = '192.168.0.1'
output: true

ip = '0.0.0.0'
output: true

ip = '123.24.59.99'
output: true

ip = '192.168.123.456'
output: false

# leading zero edge case
ip = '002.168.123.456'
output: false
'''


def validateIP(ip):
  minN = 0
  maxN = 255
  myNoSet = set(['0','1','2','3','4','5',
                '6','7','8','9'])
  #
  ipLst = split(ip, '.')
  # or using in built
  # ipLst = ip.split('.')
  
  # check if len == 4 else return false
  if not len(ipLst) == 4:
    return False
  
  # loop over each sub
  for sub in ipLst:
    # check len within expected bounds of 1 to 3
    if sub == '' or len(sub) > 3:  
      return False
    
    # leading zero
    if sub[0] == '0' and len(sub) > 1: 
      return False 
    #
    for c in sub:
      # check if not set('0','1'...'9'): False
      if not c in myNoSet:
        return False
    #
    # convert to int
    dubInt = int(sub) 
    # if resInt < minN or resInt > maxN : False
    if dubInt < minN or dubInt > maxN:
       return False
  # if no issue found: 
  return True
  



def split(ip, char='.'):
    ipLst = []
    l = 0
    for r in range(0, len(ip)):
      if ip[r] == char:
        ipLst.append(ip[l:r])
        l = r+1
      # early exit if too many dots
      if len(ipLst) > 4:
        ipLst.append('') # will make first check break
        return ipLst
    #
    ipLst.append(ip[l:len(ip)])  
    return ipLst




def testing():
  ip=  '255.255.255.255'
  print(validateIP(ip) == True)
  ip= '008.123.34.56' 
  print(validateIP(ip) == False)
  ip=  '008.1,3.34.56' 
  print(validateIP(ip) == False)
  ip=  '111..111.56' 
  print(validateIP(ip) == False)
  ip=  '255.255.255.255.255.255.255.255'
  print(validateIP(ip) == False)

testing()


  

