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
I assume that duplicate result keys will not occure.

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


# O(n) where n is number of keys in the dict
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
            else:
                rec(v, k)

    rec(dictionary, '')
    return flatt_dictionary


def flatten_dictionary_loop_and_stack(dictionary):
    if not dictionary:
        return {}
    flatt_dictionary = {}
    stack = [('', '', dictionary)]
    while stack:
        prior_key, key, value = stack.pop()
        new_key = get_new_key(prior_key, key)
        if not isinstance(value, dict):
            flatt_dictionary[new_key] = value
        else:
            for key, value in value.items():
                stack.append((new_key, key, value))
    return flatt_dictionary


def get_new_key(prior_key, key):
    if prior_key and key:
        new_key = prior_key + '.' + key
    elif prior_key:
        new_key = prior_key
    else:
        new_key = key
    return new_key


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
    print(flatten_dictionary_loop_and_stack(dictionary) == exp)

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
    print(flatten_dictionary_loop_and_stack(dictionary) == exp)

    # ex3
    dictionary = {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}
    exp = {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)
    print(flatten_dictionary_loop_and_stack(dictionary) == exp)

    # ex4
    dictionary = {"Key":{"a":"2","b":"3"}}
    exp = {"Key.a":"2","Key.b":"3"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)
    print(flatten_dictionary_loop_and_stack(dictionary) == exp)

    # ex5
    dictionary = {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}}
    exp = {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)
    print(flatten_dictionary_loop_and_stack(dictionary) == exp)

    # ex6
    dictionary = {"":{"a":"1"},"b":"3"}
    exp = {"a":"1","b":"3"}
    print(flatten_dictionary(dictionary) == exp)
    print(flatten_dictionary_done_differently(dictionary) == exp)
    print(flatten_dictionary_loop_and_stack(dictionary) == exp)

tests()
