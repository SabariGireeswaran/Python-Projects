weight = float(input("Enter weight: "))
unit = input("Convert to Kilogram/Pound(kg/lb): ").lower()

if unit == "kg":
    weight = weight / 2.205
    print(f"Weight in Kilograms: {weight:.2f} kg")
elif unit == "lb":
    weight = weight * 2.205
    print(f"Weight in Pounds: {weight:.2f} lb")
else:
    print("Invalid unit! Please choose 'kg' or 'lb'.")
