number_1 = int(input("enter number 1: "))
number_2 = int(input("enter number 2: ")) 

print("options")
print("1. number_1 / number_2")
print("2. is namber even")
print("3. hot or cold")
print("4. Large or small size")

selection = int(input(" please enter your selection "))

if selection == 1:
    if number_2 != 0:
        result = number_1 / number_2
    else:
        #   number_2 == 0
         print("number_2 is zero, setting result to 0")
    result = 0
    print(result)
elif selection == 2:
# Is number_1 even
    if number_1 % 2 == 0:
        print("number_1 is even")
    else:
         print("number_1 is odd")
elif selection == 3:    
    # Hot cold
    temp = number_1
    if temp > 20:
        print("Hot")
    else:
        # temp <=20
        print("Cold")
        # Large or smaall size
elif selection == 4:
    size = number_1
    if  size > 40:
        print("Large")
    else:
        print("small")
else:
        print("Invalid input. Option " + str(selection) + " not supported")  
