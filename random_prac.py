#to have ai complete code do ctrl + shift + P then go to Copilot: Toggle Inline Suggestions
#didn't actually use ai though because i actually want to learn
#need to seperate them so that each file has a specific topic, basically like folders
'''
# while True:
#     try:
#         age = int(input("What is your age? "))
#         if age == 20:
#             print("That's the same age as me!!!")  
#         if age < 0:
#             print("You havent been born yet, try again!!!")
#         else: 
#             break
#     except:
#         print("you need to input a number, try again")
# //////////////////////////////////////////////////////////////
#calculator programme   calc 1 
# while True:
#     operator = input("What operator do you wish to use? ")
#     num1 = float(input("What is your first number? "))
#     num2 = float(input("What is your second number? "))
hello
#     try:
#         if operator == "+":
#             ans = num1+num2
#         elif operator == "-":
#             ans = num1-num2
#         elif operator == "*":
#             ans = num1*num2
#         elif operator == "/":
#             ans = num1/num2
#         print(ans)
#         break
#     except:
#         print("it seems an operator wasnt registered, try again")
#//////////////////////////////////////////////////////////////////
# name = input("What is your name?")
# count = 0

# while bool(name) == False:
#     print("Put something in, even if it's not your name")
#     name = input("What is your name?")
#     count = 1
#     if bool(name) == True:
#         break
# if count == 1:
#     print(f"congrats, you put something in {name}")
# else:
#     print(f"Hey, {name} it's nice meeting you")
#//////////////////////////////////////////////////////////////////
# import math

# print(pow(3,3))
# result = 4.3
# bit = 1
# print(round(result))
# print(abs(result))
# print(max(result, bit))
# print(min(result, bit))
# print(math.pi)
# print(math.e)
# print(math.sqrt(math.pi * math.e))
# print(math.ceil(result))
# print(math.floor(result))
#               pow == power
# r = float(input("What is the radius? "))
# c = 2 * (math.pi * r)
# print(f"Your circumference is: {round(c, 2)}")
# a = math.pi * math.pow(r,2)
# print(f"The area of the circle is {round(a, 3)}")
#//////////////////////////////////////////////////////////////////
#weight conversion programme
# while True:
	# weight = int(input("What is your weight: "))
	# unit = input("is this in kg or lbs (K or L): ")
	# converter_weight = 0
	# kunit = ""
	# if unit == "K" or unit == "L":
	#     if unit == "K":
	#         converter_weight = weight * 2.20462
	#         kunit = "Lbs"
			
	#     elif unit =="L":
	#         converter_weight = weight/2.20462
	#         kunit = "Kg"
	#     print(f"You are {round(converter_weight)}{kunit}")
	#     break
	# else:
	#     print("please only input K for kilogram or P for pounds")
#//////////////////////////////////////////////////////////////////
# #temperature conversion programme
# unit = input("Is this unit in celsius (C/c) or fahrenheit (F/f): ").upper()
# temp = float(input("What's the temperature: "))


# if unit == "C":
#     temp = round((temp * (9/5) + 32), 2)
#     unit = "°F"
#     print(f"That is {temp}{unit}")
#     #(0°C × 9/5) + 32 = 32°F

# elif  unit == "F":
#     temp = round((temp - 32) * 5/9)
#     unit = "°C"
#     print(f"That is {temp}{unit}")
#     #(32°F − 32) × 5/9 = 0°C

# else:
#     print(f"Unit {unit} not recognised")
#//////////////////////////////////////////////////////////////////
# num = int(input("pick a number: "))
# num2 = int(input("Pick a second: "))
# result = "Even" if num % 2 == 0 else "Odd"
# max = num if num > num2 else num2
# min = num if num < num2 else num2
# print(f"the higher number is {max}")
# print(f"The lower number is {min}")
# print(result)
# age = int(input("What is your age: "))
# print("you are an adult" if age >= 18 else "You are a child")
# temp = int(input("what is the temperature in °C: "))
# stat = "It's going to be a hot day today" if temp > 15 else "It's going to be a good day today"
# print(stat)

#//////////////////////////////////////////////////////////////////
# name = input("Enter your name: ")
# s
# print(name.find("w")) #returns position where character is -1, if it cant locate it returns -1
# print(name.rfind("s")) # same as find but starts from reverse still counts from the start though, if it cant locate it returns -1
# name = name.capitalize()
# print(name)
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# phone_number = input("What is your phone number: ")
# result = phone_number.replace(" ", "") #replaces any occurance of first bracket with second bracket
# print(result)
# print(help(str)) #shows different methods
#//////////////////////////////////////////////////////////////////
# user_name = ""
# space = 0
# digit = 0

# user_name = input("What would you like your username to be? ")

# while len(user_name) > 12 or space > 0 or digit > 0:

	# space = 0
	# digit = 0
	# user_name = input("What would you like your username to be? ")
	
	# for character in user_name: 
	#     if character.isdigit():
	#         digit += 1
	
	# for i in user_name:
	#     if i == " ":
	#         space += 1

	
#not finished, need to fix so checks are done properly
#//////////////////////////////////////////////////////////////////
'''
# ''' comments several lines, three before and afrter
#Reversing numbers
# card_number = "1234 2345 3456 4567 5678"

# length = len(card_number)
# i = 0

# reverse = [0] * length

# while i < length:
#     reverse[length - 1 - i] = card_number[i]
#     i += 1
# print("".join(reverse))
# #//////////////////////////////////////////////////////////////////
# card_number = "1234 2345 3456 4567 5678"
# i = 0
# length = len(card_number)
# reverse = [0] * length

# while i < length:
#     reverse[i] = card_number [length - i - 1]
#     i += 1
# print("".join(reverse))
# #did again to make sure i can actually do it (i did)
#//////////////////////////////////////////////////////////////////
#Format specifiers
#.2f means print the variables to 2 decimal places (float),
#if i did :10 it would give each value 10 spaces instead (it'll make spaces to reach it), 
#put <10 it'll put the spaces in after A.K.A left justified & > puts the spaces before A.K.A Right justified,
#^ gives centred aligned,
#+ if you want a number to display as a +____ if its positive, if negative it wont affect,
#, separates the thousands
#to do several do them back to back


# number1 = 25.23442
# number2 = 27.34543
# number3 = 28.56782

# print(f"Your first is {number1:.2f}, second is {number2:^10}, third is {number3:.1f} 😊😊")
#//////////////////////////////////////////////////////////////////
#A=P(1+ R/N =)^t

# 'A = final amount'
# P = 0 #(initial principal balance)
# R = 0 #(interest rate)
# T = 0 #number of time periods elapsed(years)
# N = 3 #how often interest is paid

# while True:
# 	P = float(input("What is the value for the initial principal balance: "))
# 	if P < 0:
# 		P = float(input("Your value must be greater then 0, try again: "))
# 	else:
# 		break
# while True:
# 	R = float(input("What is the value for the interest rate: "))
# 	if R < 0:
# 		R = float(input("Your value must be greater then 0, try again: ")) 
# 	else:
# 		break   
# while True:
# 	T = int	(input("What is the value for the number of time periods elapsed(years): "))
# 	if T < 0:
# 		T = int(input("Your value must be greater then 0, try again: "))
# 	else:
# 		break

# A = P*(1 + (R/N)) ** T
# print(f"Your final amount after {T} years: £{A:.2f}")
# #chatgpt says its wrong but i followed instruction from 
#//////////////////////////////////////////////////////////////////
#for loops
# for x in range(1, 11):
#     print(x)
# for x in reversed(range(1, 11)):
# 	print(x)
# print ("Happy New year!!!")
# for x in range(1,11,-1):
# 	print(x)
#structured (inclusive, exclusive, step up/down)

#to have ai complete code do ctrl + shift + P then go to Copilot: Toggle Inline Suggestions

# for i in range(1,22):
# 	if i == 13:
# 		continue ##allows me to skip printing 13
#		break ##stops the loop
# 	else:
# 		print(i) 
#//////////////////////////////////////////////////////////////////
# % returns the remainder of a division
#timer
#this one i kept checking the solution😔🥲
# import time

# timer = int(input("What is the time amount: "))

# for i in range (timer, 0 , -1):
# 	seconds = i % 60
# 	minutes = int(i/60) % 60
# 	hours = int(i/3600) % 60
# 	print(f"{hours:02}:{minutes:02}:{seconds:02}")
# 	time.sleep(1)

# print("Times Up!!!!!")

#//////////////////////////////////////////////////////////////////
#cs50 c exercise - DONE WITHOUT ANY HELP!!!!!!!!, main issue was the logic behind it not the code itself
# number = int(input("pick the size of your pyramid:"))

# for x in range(0, number, 1):
# 	for y in range(0, number, 1):
# 		if(y < number - x - 1):
# 			print(" ", end = "")
# 		else:
# 			print("*", end = "")
# 	print(" ", end = "")#
# 	for k in range(0, number, 1):
# 		if k in range(x+1):
# 			print("*", end = "")
# 	print("")
		
#//////////////////////////////////////////////////////////////////
#to make it so that everything stayson the same line do print(___, end="")
#//////////////////////////////////////////////////////////////////
#timer solution without any help
# import time
# import winsound 

# name = input("Hey, welcome to this timer system, what would you like me to call you? ")
# time.sleep(1)
# timer = int(input(f"Hi {name}, how long would you like the timer to go for: "))
# time.sleep(1)
# wait = int(input(f"Almost done {name}, how much time would you like before the timer starts once you've given the go ahead? "))
# beep = int(input("Lastly,how many times would you like the beep to happen? "))
# time.sleep(1)
# random = (input("enter anything to get the timer started..."))
# time.sleep(wait)
# for i in range (timer, 0, -1):
# 	second = i%60
# 	minutes = int(i/60)%60
# #doing // gives you the whole number when you divided
# 	hours = (i//3600)%60
# 	print(f"{hours:02}:{minutes:02}:{second:02}")
# 	time.sleep(1)
# print("Times Up!!!!!")

# for i in range(beep):
# 	winsound.Beep(800, 500)

# print(f"Congratulations {name}, you've completed the system, bye😁😁")
#success
#//////////////////////////////////////////////////////////////////
#nested for loops
# rows = int(input("enter the number of rows: "))
# columns = int(input("enter the number of columns: "))
# symbol = input("What symbol would you like to get printed: ")

# for i in range(0, rows, 1):
# 	for j in range(0, columns, 1):
# 		print(symbol, end = "")
# 	print()
#//////////////////////////////////////////////////////////////////
#collections: 
#Lists[]ordered and changeable - duplicates are ok,
#Set{}unordered and immutable, but Add/Remove OK. NO duplicates,
#tuple()ordered and unchangeable. Duplicates OK. FASTER

#print(dir(collection name)) tells you the different functions availible to a collection
#print(help(collection name)) gives description of all methods and attributes

# colours = ["black", "grey", "white", "navy"]
# no = "tomato"
# i = 0

# for colour in colours: 
# 	print(colour)

# print()

# colours.append("Milkshake")

# for colour in colours:
# 	print(colour)

# colours.remove("white")
# colours.insert(2, "grey")
#colours.sort()
#colours.reverse
# colours.clear()

# print()
# for colour in colours:
# 	print(colour)

# print(colours.index("black"))
# print(colours.count("white"))
# revo = list(reversed(colours))
# while i < len(revo):
# 	print(str(revo[i]))
# 	i +=1

# print()
# print(no in colours)

# letters = {"mb", "km", "ci", "mbr"}
# letters.add("jo")
# letters.remove("jo")
# letters.pop()

# print(letters)


#//////////////////////////////////////////////////////////////////
print("Hello, world")
#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
