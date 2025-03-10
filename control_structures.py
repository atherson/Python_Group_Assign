#input radius of sphere
#compute volume and surface area of the sphere
#computed values displayed using an appropriate format


def measurement():
    1 == "cm"
    2 == "m"

print(f"1 = cm")
print(f"2 = m")

# Only allow input between 1 and 2 using a while loop
# 1 for metre and 2 for centimetre
while True:
    try:
        measurement = int(input("Choose 1 for cm and 2 for m: "))
        if measurement == 1:
            break
        if measurement == 2:
            break
        else:
            print("\n Invalid Input only pick between 1 or 2\n".upper())
    except ValueError:
        print("Invalid Input! Kindly Input an Integer!".upper())

if measurement == 1:
    radius = float(input("What is the radius of the sphere: "))
    pi = 3.142
    print(f"Radius = {radius} cm" .upper())
    volume = round(4/3*pi*radius**3)
    surface = round(4*pi**2)
    print(f"The surface area of the sphere is {surface} cm\u00B2")
    print(f"The volume of the sphere is {volume} cm\u00B3")
else:
    radius = float(input("What is the radius of the sphere: "))
    pi = 3.142
    print(f"Radius = {radius} m".upper())
    volume = round(4/3*pi*radius**3)
    surface = round(4*pi**2)
    print(f"The surface area of the sphere is {surface} m\u00B2")
    print(f"The volume of the sphere is {volume} m\u00B3")







