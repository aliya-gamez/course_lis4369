def get_requirements():
    print("\nDeveloper: Aliya Gamez\n")
    print("Program Requirements:\n"
            + "1. Dictionaries (Python data structure): unordered key:value pairs.\n"
            + "2. Dictionary: an associative array (also known as hashes).\n"
            + "3. Any key in dictionary is associated (or mapped) to a value (i.e, any Python data type).\n"
            + "4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique.\n"
            + "5. Values: can be any data type and can repeat.\n"
            + "6. Create a program that mirrors the following IPO (input/process/output) format.\n"
            + "\tCreate empty dictionary, using curly braces {}: my_dictionary = []"
            + "\tUse the following keys: fname, lname, degree, major, gpa\n"
            + "Note: Dictionaries have key-value pairs instead of single values; this differentiates a dictionary from a set\n")

def python_dictionaries():
    #DECLARTIONS
    fname = ""
    lname = ""
    degree = ""
    major = ""
    gpa = 0.0
    my_dictionary = {}
    
    #CODE
    print("Input: ")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    degree = input("Degree: ")
    major = input("Major (IT or ICT): ")
    gpa = float(input("GPA: "))
    
    my_dictionary['fname'] = fname
    my_dictionary['lname'] = lname
    my_dictionary['degree'] = degree
    my_dictionary['major'] = major
    my_dictionary['gpa'] = gpa

    print("\nOutput:")
    print("Print my_dictionary:")
    print(my_dictionary)

    print("\nReturn view of dictionary's (key, value) pair, built-in function:")
    print(my_dictionary.items())

    print("\nReturn view object of all keys, built-in function:")
    print(my_dictionary.keys())

    print("\nReturn view object of all values in dictionary, built-in function:")
    print(my_dictionary.values())

    print("\nPrint only first and last names, using keys: ")
    print(my_dictionary['fname'], my_dictionary['lname'])

    print("\nPrint only first and last names, using get() function:")
    print(my_dictionary.get("fname"),my_dictionary.get("lname"))

    print("\nCount number of items (key: value pairs) in dictionary: ")
    print(len(my_dictionary))

    print("\nRemove last dictionary item (popitem): ")
    my_dictionary.popitem()
    print(my_dictionary)

    print("\nDelete major from dictionary, using key: ")
    my_dictionary.pop("major")
    print(my_dictionary)

    print("\nReturn object type: ")
    print(type(my_dictionary))

    print("\nDelete all items from list: ")
    my_dictionary.clear()
    print(my_dictionary)

    del my_dictionary