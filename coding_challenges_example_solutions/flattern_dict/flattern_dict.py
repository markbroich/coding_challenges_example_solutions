# def flatten_dictionary(dictionary):
  
#   def rec(key, value):
#     if not isinstance(value, dict):
#       return value
#     value_x = {}
#     for k, v in value.items():
#       kx, vx = rec(k, v)
#       value_x[k + '.' + kx] = vx
#     return value_x
#   res = {}
#   for k_outer, v_outer in dictionary.items():
#     ky, vy = rec(k_outer, v_outer)
#     print(ky, vy)
#     res[ky] = vy
#   return res
  

'''Flatten a Dictionary

A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).


Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }

Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

Constraints:

[time limit] 5000ms
[input] Dictionary dict
[output] Dictionary
'''


# O(n) where n is number of keys in the dict
def flatten_dictionary(dictionary):
    if not dictionary:
        return {}

    def rec(my_dict):
        flattened = {}
        for k, v in my_dict.items():
            if not isinstance(v, dict):
                flattened[k] = v
            else:
                for kx, vx in rec(v).items():
                    if not k:
                        flattened[kx] = vx
                    elif not kx:  # skip empty key
                        flattened[k] = vx
                    else:
                        flattened[k + '.' + kx] = vx
        return flattened
    return rec(dictionary)













def flatten_dictionary_done_differently(dictionary):
    if not dictionary:
        return {}
    flatt_dictionary = {}

    def rec(input, key):
        if not isinstance(input, dict):
            flatt_dictionary[key] = input
            return
        for k, v in input.items():
            if key and k:
                rec(v, key + '.' + k)
            elif key:
                rec(v, key)
            else: rec(v, k)

    rec(dictionary, '')
    return flatt_dictionary


def tests():
    # ex 1
    dictionary = {
            "Key1" : "1",
            "Key2" : {"a" : "2"}
    }
    exp = {
            "Key2.a" : "2", 
            "Key1" : "1",}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)

    # ex2 
    dictionary = {
                "Key1" : "1",
                "Key2" : {
                    "a" : "2",
                    "b" : "3",
                    "c" : {
                        "d" : "3",
                        "e" : {
                            "" : "1"
                        }
                    }
                }
            }
    exp = {
                "Key1" : "1",
                "Key2.a" : "2",
                "Key2.b" : "3",
                "Key2.c.d" : "3",
                "Key2.c.e" : "1"
            }
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)  

    # ex3
    dictionary = {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}
    exp = {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)  

    # ex4
    dictionary = {"Key":{"a":"2","b":"3"}}
    exp = {"Key.a":"2","Key.b":"3"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)  

    # ex5
    dictionary = {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}}
    exp = {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)  

    # ex6
    dictionary = {"":{"a":"1"},"b":"3"}
    exp = {"a":"1","b":"3"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)  

tests()



def flattenKeyVal(inputDict):
  flattenedDict = {}
  
  for key in inputDict:
      if isinstance(inputDict[key], str) or isinstance(inputDict[key], int):
         flattenedDict[key] = inputDict[key]
      else:
          tmpInputDict = flattenKeyVal(inputDict[key])
          for tmpKey in tmpInputDict:
              newKey = ''
              if key == '':
                newKey = tmpKey
              elif tmpKey == '':
                newKey = key
              else: 
                newKey = key + '.' + tmpKey
              flattenedDict[newKey] = tmpInputDict[tmpKey]
  return flattenedDict
      