def fuel_cost(distance_miles):
    # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...
    #How many gallons of fuel used
    gallons = distance_miles / MPG  
    #How many litres of fuel used 
    litres = gallons * LITERS_PER_GALLON
    #Price of litres of fuel used
    total_cost = litres * PRICE_PER_LITER   
    return total_cost
print(fuel_cost(50))