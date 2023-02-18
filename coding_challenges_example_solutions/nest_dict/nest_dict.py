'''
Task is to turn a dictionary into a nested
dictionary where each "." deliniates a subkey.

Example:
dictionary = {
        "Key2.a" : "2",
        "Key1" : "1",}
expected = {
        "Key1" : "1",
        "Key2" : {"a" : "2"}
    }
'''


def nest_dict(dictionary):
    nested_dict = {}
    for k, v in dictionary.items():
        key_lst = k.split(('.'))
        if len(key_lst) == 1:
            nested_dict[k] = v
        else:
            temp_dict = nested_dict
            for i in range(0, len(key_lst) - 1):
                nk = key_lst[i]
                if nk not in temp_dict:
                    temp_dict[nk] = {}
                temp_dict = temp_dict[nk]
            temp_dict[key_lst[i + 1]] = v
    return nested_dict


def tests():
    # ex 1
    dictionary = {
            "Key2.a" : "2", 
            "Key1" : "1",}
    expected = {
            "Key1" : "1",
            "Key2" : {"a" : "2"}
    }
    print(nest_dict(dictionary) == expected)

    # ex2
    dictionary = {
                "Key1" : "1",
                "Key2.a" : "2",
                "Key2.b" : "3",
                "Key2.c.d" : "3",
                "Key2.c.e" : "1"
            }
    expected = {
                "Key1" : "1",
                "Key2" : {
                    "a" : "2",
                    "b" : "3",
                    "c" : {
                        "d" : "3",
                        "e" : "1"
                    }
                }
            }
    print(nest_dict(dictionary) == expected)

    # ex3
    dictionary = {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"}
    expected = {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}
    print(nest_dict(dictionary) == expected)

    # ex4
    dictionary = {"Key.a":"2","Key.b":"3"}
    expected = {"Key":{"a":"2","b":"3"}}
    print(nest_dict(dictionary) == expected)

    # ex5
    dictionary = {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"}
    expected = {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}}
    print(nest_dict(dictionary) == expected)

    # ex6
    dictionary = {"a":"1","b":"3"}
    expected = {"a":"1","b":"3"}
    print(nest_dict(dictionary) == expected)


tests()
