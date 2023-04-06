def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Python Sets -- Like mathematical sets!")
    print("\nProgram Requirements:"
        + "\n1. Sets (Python data struct): mutable, heterogenus, unordered sequence of elements, but cannot hold duplicate values"
        + "\n2. Sets are mutable/changeable -- that is, update, insert, and deletable"
        + "\n3. While sets are mutable, they *cannot* contain other mutable items like lists, sets, or dictionary--"
        + "\n\tthat is, elements contained in set must be immutable"
        + "\n4. Also, since sets are unordered, cannot use indexing (or, slicing) to access, update, or delete objects"
        + "\n5. Two methods to create sets:"
        + "\n\ta. Create set using curly brackets \{set\}: my_set = {1, 3.14, 2.0, 'four', 'Five'}"
        + "\n\tb. Create set using set() function: my_set = set(<iterable>)"
        + "\n\tExamples:"
        + "\n\tmy_set = set([1, 3.14, 2.0, 'four', 'Five']) set with list"
        + "\n\tmy_set = set((1, 3.14, 2.0, 'four', 'Five')) set with tuple"
        + "\n\tNOTE: an \"iterable\" is *any* object that can be iterated over, that is, lists, tuples, ore even strings"
        + "\n6. Create a program that mirrors the follwing IPO Format\n")
    
def python_sets():
    #CODE
    print("\nInput hard coded, no user input.")
    print("\n***Note***: All three sets below print as \"sets\" (i.e. curly brackets) *regardless* of how they were created")

    my_set = {1, 3.14, 2.0, 'Five', 'four'}
    print("\nPrint my_set created using curly brackets:")
    print(my_set)

    print("\nPrint type of my_set:")
    print(type(my_set))

    my_set1 = set({1, 3.14, 2.0, 'Five', 'four'})
    print("\nPrint my_set1 created using set() function with list:")
    print(my_set1)

    print("\nPrint type of my_set1:")
    print(type(my_set1))

    my_set2 = set({1, 3.14, 2.0, 'Five', 'four'})
    print("\nPrint my_set2 created using set() function with tuple:")
    print(my_set2)

    print("\nPrint type of my_set2:")
    print(type(my_set2))

    print("\nLength of my_set:")
    print(len(my_set))

    print("\nDiscard 'four'")
    my_set.discard('four')
    print(my_set)

    print("\nRemove 'Five'")
    my_set.remove('Five')
    print(my_set)

    print("\nLength of my_set:")
    print(len(my_set))
    
    print("\nAdd element to set (4) using add() method:")
    my_set.add(4)
    print(my_set)
    
    print("\nLength of my_set:")
    print(len(my_set))
    
    print("\nDisplay minimum number:")
    print(min(my_set))

    print("\nDisplay maximum number:")
    print(max(my_set))
    
    print("\nDisplay sum of numbers:")
    print(sum(my_set))

    print("\nDelete all set elements:")
    my_set.clear()
    print(my_set)

    print("\nLength of my_set:")
    print(len(my_set))
    
