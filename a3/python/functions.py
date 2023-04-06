# CONSTANT VALUES
SQFT_PER_GALLON = 350

def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Painting Estimator")
    print("\nProgram Requirements:"
          + "\n1. Calculate home interior paint cost (w/o primer)."
          + "\n2. Must use float data types."
          + "\n3. Must use SQFT_PER_GALLON constant (350)."
          + '\n4. Must use iteration structure (aka "loop").'
          + "\n5. Format, right-align numbers, and round to two decimal places."
          + "\n6. Create at least five functions that are called by the program:"
          + "\n\ta. main(): calls two other functions: get_requirements() and estimate_painting_cost()"
          + "\n\tb. get_requirements(): displays the program requirements."
          + "\n\tc. estimate_painting_cost(): calculates interior home painting, and calls print functions."
          + "\n\td. print_painting_estimate(): displays painting costs."
          + "\n\te. print_painting_percentage(): displays painting costs percentages.")
    
def estimate_painting_cost():
    print("\nInput:")
    totalSqft = float(input("Enter total interior sq ft: "))
    priceGallon = float(input("Enter price per gallon paint: "))
    laborSqft = float(input("Enter hourly painting rate per sq ft: "))
    print("\n")
    
    numGallon = totalSqft / SQFT_PER_GALLON
    paintTotal = numGallon * priceGallon
    laborTotal = totalSqft * laborSqft
    total = paintTotal + laborTotal
    
    print_painting_estimate(totalSqft, numGallon, priceGallon, laborSqft)
    print_painting_percentage(paintTotal, laborTotal, total)
    
    paintContinue = str(input("\nEstimate another paint job? (y/n): "))
    
    if paintContinue == "y":
        estimate_painting_cost()
    else:
        print("\nThank you for using our Painting Estimator!\nPlease see our web site: http://www.mysite.com")
        
    
def print_painting_estimate(totalSqft, numGallon, priceGallon, laborSqft):  
    rule = "{0:<22} {1:>9,.2f}"
    rule_mon = "{0:<22} ${1:>8,.2f}"
    label = "{0:<22} {1:>9}"
    print("Output:")
    print(label.format('Item','Amount'))
    print(rule.format('Total Sq Ft:', totalSqft))
    print(rule.format('Sq Ft per Gallon:', SQFT_PER_GALLON))
    print(rule.format('Number of Gallons:', numGallon))
    print(rule_mon.format('Price per Gallon:', priceGallon))
    print(rule_mon.format('Labor per Sq Ft:', laborSqft))
    
        
def print_painting_percentage(paintTotal, laborTotal, total):
    rule = "{0:<8} ${1:>8,.2f} {2:>13.2f}%"
    label = "{0:<8} {1:>9} {2:>14}"
    print("\n")
    print(label.format('Cost', 'Amount', 'Percentage'))
    print(rule.format('Paint:', paintTotal, ((paintTotal/total)*100) ))
    print(rule.format('Labor:', laborTotal, ((laborTotal/total)*100) ))
    print(rule.format('Total:', laborTotal+paintTotal, 100))
    
