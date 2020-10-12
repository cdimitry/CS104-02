
#Christian Dimitry

temp = int(input ("Please enter current temp: "))
while (temp != 999):
    if (temp > 90):
        print("Wear shorts")
        temp = int(input("Please enter current temp: "))
    elif (temp > 70):
        print("Short sleeves are fine")
        temp = int(input("Please enter current temp: "))
    elif (temp > 50):
        print("Wear jacket")
        temp = int(input("Please enter current temp: "))
    elif (temp > 32):
        print("Wear heavy coat")
        temp = int(input("Please enter current temp: "))
    else:
        print ("Stay inside")
        temp = int(input("Please enter current temp: "))
    if (temp == 999):
        break
