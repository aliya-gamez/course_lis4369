def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Python Lists")
    print("\nProgram Requirements:"
          + "\n1. Lists (Python data structure): mutable, ordered sequence of elements."
          + "\n2. Lists are mutable/changeable--that is, can isnert, update, delete."
          + "\n3. Create list - using square brackets [list]: my_list = [\"cherries\", \"apples\", \"bananas\", \"oranges\"]."
          + "\n4. Create a program that mirror the following IPO (input/process/output) format."
          + "\nNote: user enters number of requested list elements, dynamically rendered below (that is, number of elements can change each run).\n")
    
def python_lists():
    #CODE
    print("\nInput")
    listSize = int(input("\nEnter number of list elements: "))
    
    my_list = []
    
    for i in range(listSize):
        element = str(input("\nPlease enter list element " + str(1+i) + ": "))
        my_list.append(element)
        
    print("\nOutput:")
    print("Print my_list:")
    print(my_list)
    
    exactElement = str(input("Please enter list element: "))
    indexElement = int(input("Please enter list *index* position (note: must convert to int): "))
    
    print("\nInsert element into specific position in my_list")
    my_list.insert(indexElement, exactElement)
    print(my_list)
    
    print("\nCount number of elements in list: ")
    print(len(my_list))
    
    print("\nSort elements in list alphabetically: ")
    my_list.sort()
    print(my_list)
    
    print("\nReverse List: ")
    my_list.reverse()
    print(my_list)

    print("\nRemove last list element: ")
    my_list.pop()
    print(my_list)

    print("\nDelete second element from list by *index*. (note 1 = second item): ")
    del my_list[1]
    print(my_list)

    print("\nDelete element from list by *value* (cherries): ")
    my_list.remove('cherries')
    print(my_list)

    print("\nDelete all elements from list: ")
    my_list.clear()
    print(my_list)
