weight= float(input("Enter your weight: "))
unit= input("Kilograms or Pounds? (K or L): ").strip().upper() # Removes spaces and converts input to uppercase

if unit == "K":
    weight = weight * 2.205
    print(f"Your weight is: {round(weight, 1)} Lbs.")

elif unit == "L":
    weight = weight/2.205
    print(f"Your weight is: {round(weight,1)} Kgs.") 

else:
    print(f"{unit} is not valid.Please enter 'K' for Kilograms or 'L' for Pounds.")    