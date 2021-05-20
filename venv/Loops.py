fruits = ["apple", "orange", "kiwi", "mango", "chery", "grapes"]

for fruit in fruits:
    print("would you like {} ?".format(fruit))


for number in range(1,11):
    print("Number {} ".format(number))



temp_c = 100

while temp_c > 90:
    print("The water boils at {} ".format(temp_c))
    temp_c -= 1


#Loop statement

#Break - END the loop go to the next statement in the program (Outside the loop)

temp_c = 100
while temp_c > 90:
    print("The water boils at {} ".format(temp_c))
    temp_c -= 1
    if temp_c == 94:
        break

#Continue - Skips current part of the loop, move to the next part of the loop

for number in range(1,11):
    if number ==7:
        print("Skip the number 7")
        continue
    print("Number {} ".format(number))



#Pass - Skips sny part of the loop where "pass " appears, best used for testing code