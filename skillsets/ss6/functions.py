def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Python Looping Structures")
    print("\nProgram Requirements:"
          + "\n1. Print while loop."
          + "\n2. Print for loops using range() function, and implicit and explicit lists."
          + "\n3. Use break and continue statements."
          + "\n4. Replicate display below." 
          + "\nNote: In Python, for loop used for iterating over a sequence (i.e. list, tuple, dictionary, set, or string).\n")
    
def print_python_loops():
    print("\n1. while loop:")
    x = 0
    while x <= 3:
        print(x)
        x += 1
    
    print("\n2. for loop: using range() function with 1 arg")
    for i in range(4):
        print(i)
    
    print("\n3. for loop: using range() function with two args")
    for i in range(1, 4):
        print(i)
    
    print("\n4. for loop: using range() function with three args (interval 2):")
    for i in range(1, 4, 2):
        print(i)
    
    print("\n5. for loop: using range() function with three args (negative interval): ")
    for i in range(3, 0, -2):
        print(i)
    
    print("\n6. for loop using (implicit) list (i.e, list not assigned to variable):")
    for i in [1, 2, 3]:
        print(i)
        
    print("\n7. for loop iterating through (explicit) string list:")
    list = ['Michigan', 'Alabama', 'Florida']
    for i in list:
        print(i)
        
    print("\n8. for loop using break statement (stops loop):")
    for i in list:
        if(i == "Alabama"):
            break
        print(i)
    
    print("\n9. for loop using continue statement (stops and continues with next):")
    for i in list:
        if(i == "Alabama"):
            continue
        print(i)
    
    print("\n10. print list length:")
    print(len(list))
    