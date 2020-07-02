# python basics
print("Hello, Joshua")
print("""It's very cold outside
isn't it?""")

# math caculations
print(7)
print(1+1)

# string tricks
print("Hello" + "there")
print("Hello" * 5)

# Asking for numbers
age = int(input("How old are you?"))
age_in_10 = age + 10
print("In 10 years you will be {}" .format(age_in_10))

# Varying variables
number = 10
number += 5 # Adds 5, number is 15
number -= 5 # Subtracts 5, number is 10
number *= 5 # Multiplies 5, number is 50
number /= 5 # Divides 5, number is 10 again
print(number)

score = 0
 
answer = input("What does CPU stand for?")
if answer == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")
  
answer = input("How many bits are in a byte?")
if answer == "8":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")
  
answer = input("Which is bigger: a kilobyte or a megabyte?")
if answer == "megabyte":
  print("Correct!")
  score += 1
else:
  print("Sorry, wrong answer.")
 
print("You scored {} points!".format(score))
