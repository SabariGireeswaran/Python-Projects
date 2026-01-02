unit = input("Enter the unit you want to convert from (C for " \
"Celsius, F for Fahrenheit): ").strip().upper()
temperature = float(input("Enter the temperature value to" \
"convert: "))

if unit == 'C':
    temperature = round((temperature * 9) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is {temperature}F")
elif unit == 'F':
    temperature = round((temperature - 32) * 5 / 9, 2)
    print(f"The temperature in Celsius is {temperature}C")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
