import random

def get_requirements():
    print("Developer: Aliya Gamez")
    print("Temperature Conversion Program")
    print("\nProgram Requirements:\n"
            + "1. Program converts user-entered temperatures into farenheit or celsius scales.\n"
            + "2. Program continues to prompt for user entry until no longer requested.\n"
            + "3. Note: Upper or lower case letter permitted. Though, incorrect entries are not permitted.\n"
            + "4. Note: Program does not validate numeric data (optional requirement).\n"
            + "5. Values: can be any data type and can repeat.\n")

def temperature_conversion():
    #DECLARTIONS
    temp = 0.0
    prompt = ' '
    type = ' '
   
    print("\nInput:")
    prompt = input("Do you want to convert a temperature (y or n)?: ").lower()

    print("\nOutput:")
    while(prompt == 'y'):
        type = input("Fahrenheit to Celsius? Type \"f\", or for Celsius to Fahrenheit? Type \"c\": ").lower()
        if type == 'f':
            temp = float(input("Enter temperature in Fahrenheit: "))
            temp = (((temp-32)*5)/9)
            print("Temperature in Celsius = " + str(temp))
            prompt == input("\nDo you want to convert another temperature (y or n)?: ").lower()
        elif type == 'c':
            temp = float(input("Enter temperature in Celsius: "))
            temp = ((temp * 9/5) + 32)
            print("Temperature in Fahrenheit = " + str(temp))
            prompt = input("\nDo you want to convert another temperature (y or n)?: ").lower()
        else:
            print("Incorrect entry. Please try again.")
            prompt = input("\nDo you want to convert a temperature (y or n)?: ").lower()
        
    print("\nThank you for using our Temperature Conversion Program!")
