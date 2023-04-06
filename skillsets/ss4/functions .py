def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Calorie Percentage")
    print("\nProgram Requirements:"
          + "\n1. Find calories per grams of fat, carbs, and protein."
          + "\n2. Calculate percentages."
          + "\n3. Must use float data types."
          + "\n4. Format, right-align numbers, and round to two decimal places.\n")
    
def calculate_calorie_percentage():
    totalFat = 0.0
    totalCarb = 0.0
    totalProtein = 0.0
    totalMacro = 0.0
    calorieFat = 0.0
    calorieCarb = 0.0
    calorieProtein = 0.0
    percentFat = 0.0
    percentCarb = 0.0
    percentProtein = 0.0
    
    print("Input:")
    totalFat = float(input("Enter total fat grams: "))
    totalCarb = float(input("Enter total carb grams: "))
    totalProtein = float(input("Enter total protein grams: "))
    
    calorieFat = totalFat * 9
    calorieCarb = totalCarb * 4
    calorieProtein = totalProtein * 4
    
    totalCalorie = calorieFat + calorieCarb + calorieProtein
    
    percentCarb = (calorieCarb / totalCalorie) *100 
    percentFat = (calorieFat / totalCalorie) * 100
    percentProtein = (calorieProtein / totalCalorie) * 100
    
    print("\nOutput:")
    label = "{0:<8} {1:>8} {2:>13}"
    rule = "{0:<8} {1:>8,.2f} {2:>13.2f}%"
    print(label.format('Type', 'Calories', 'Percentage'))
    print(rule.format('Fat', calorieFat, percentFat))
    print(rule.format('Carbs', calorieCarb, percentCarb))
    print(rule.format('Protein', calorieProtein, percentProtein))
    