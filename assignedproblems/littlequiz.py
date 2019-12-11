yes = input("Are you ready for a quiz? ")
yes = True
count = 0
print("Good! Here it is.")
ans0 = int(input("What is the capital of Alaska? Enter in option numbers. \n1: Melbourne\n2:Anchorage \n3:Juneau \n"))
if ans0 == 3:
    print("correct")
    count += 1
else:
    print("NO")
ans1 = input("Can you store the value \"cat\" in a variable type int? yes or no will sufice as answers.\n")
if ans1 == "no" or ans1 == "No":
    print("correct")
    count += 1
else:
    print("FALSE")
ans2 = int(input("What is 9+6/3 equal to? Input only integer responses\n"))
if ans2 == 11:
    print("Correct")
    count += 1
else:
    print("FALSE")
print("You got", count, "answers correct.")