print("UNIT CONVERTER")
print("1. Kilometers to Meters")
print("2. Celsius to Fahrenheit")

choice = int(input("Enter your choice: "))

if choice == 1:
    km = float(input("Enter kilometers: "))
    print("Meters =", km * 1000)
elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit =", (celsius * 9/5) + 32)
else:
    print("Invalid choice")
