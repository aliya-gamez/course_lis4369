def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Python Tuples")
    print("\nProgram Requirements:\n"
        + "1. Tuples (python data structure): *immutable* (cannot be changed!), ordered sequence of elements\n"
        + "2. Tuples are immutable/unchangable: cannot update, insert, or delete.\n"
        + "Note: can reassign or delete an *entire* tuple\n"
        + "3. Create tuple using parenthesis (tuple): my_tuple = (\"cherries\", \"apples\", \"bananas\", \"oranges\")\n"
        + "4. Create tuple (packing) without using parenthesis\n"
        + "5. Python tuple (unpacking) that is, assign values from tuple to variables: fruit1-4\n"
        + "6. Create a program that mirrors the follwing IPO format\n")
    
def python_tuples():
    #CODE
    print("\nInput hard coded, no user input.")
    my_tuple1 = ("cherries", "apples", "bananas", "oranges")
    my_tuple2 = (1, 2, "three", "four")

    print("\nOutput:")
    print("Print my_tuple1:")
    print(my_tuple1)

    print("\nPrint my_tuple2:")
    print(my_tuple2)

    fruit1, fruit2, fruit3, fruit4 = my_tuple1
    print("\nPrint my_tuple1 unpacking:")
    print(fruit1, fruit2, fruit3, fruit4)

    print("\nPrint third element in my_tuple2")
    print(my_tuple2[2])

    print("\nPrint \"slice\" of my_tuple1 (second and third elements)")
    print(my_tuple1[1:3])

    print("\nReassign my_tuple2 using parenthesis")
    my_tuple2 = (1, 2, 3, 4)
    print("Print my_tuple2:")
    print(my_tuple2)

    print("\nReassign my_tuple2 using \"packing\" method (no parenthesis)")
    my_tuple2 = (5, 6, 7, 8)
    print("Print my_tuple2")
    print(my_tuple2)

    print("\nPrint number of elements in my_tuple1: " + str(len(my_tuple1)))

    print("\nPrint type of my_tuple1: " + str(type(my_tuple1)))

    print("\nDelete my tuple1:")
    print("\nNote: will generate error if trying to print after, as it no longer exists")
    del my_tuple1
    
