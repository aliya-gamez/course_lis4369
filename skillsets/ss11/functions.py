import random

def get_requirements():
    print("Developer: Aliya Gamez")
    print("Psuedo-Random Number Generator")
    print("\nProgram Requirements:\n"
          + "1. Get user beginning and ending integer values, and store in two variables.\n"
          + "2. Display 10 psuedo-random numbers between, and includong, above values.\n"
          + "3. Must user integer data types.\n"
          + "4. Example 1: Using range() and randint() functions."
          + "5. Example 2: Using a list with range() and shuffle() functions.")

def number_generator():
    #DECLARATIONS
    beginningValue = 0
    endValue = 0

    #CODE
    print("\nInput: ")
    beginningValue = int(input("Enter beginning value: "))
    endValue = int(input("Enter ending value: "))

    print("\nOutput: ")
    print("Example 1: Using range() and randint() functions:")
    for item in range(10):
        print(random.randint(beginningValue, endValue), end = " ")

    print("\n\nExample 2: Using a list, with range() and shuffle() functions:")
    intList = list(range(beginningValue, endValue + 1))
    random.shuffle(intList) 
    for item in intList:
        print(item, end = " ")
    print()