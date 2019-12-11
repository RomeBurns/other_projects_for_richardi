mass = int(input("what is your weight in pounds on Earth? "))
planet = int(input("I have information for the following planets. Enter the number corresponding to the planet you wish to know your weight on: \n 1:Venus    2:Mars    3:Jupiter    4:Saturn    5:Uranus    6:Neptune \nChosen Planet: "))
if planet == 1:
    print(mass * 0.78)
elif planet == 2:
    print(mass * 0.39)
elif planet == 3:
    print(mass * 2.65)
elif planet == 4:
    print(1.17 * mass)
elif planet == 5:
    print(mass * 1.05)
elif planet == 6:
    print(mass * 1.23)
print("Next time use the metric system, and we won't have this problem.")