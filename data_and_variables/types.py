print(int("33"))
newVariable = 'hello'
num = 6
print(num)
print(type(newVariable))


# changing variable types:
variable1 = 1
print("variable1 is of type", type(variable1))
variable1 = 'hello'
print("variable1 is of type", type(variable1))

# naming conventions:
#     Use only the characters 0-9, a-z, A-Z, and underscore. 
#     Do not start a variable name with a number.
#     Do not use keywords, which are words reserved by Python

# Operations:
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 ** 3)
print(3 ** 2)

# // :
# divides two numbers and rounds the result down to the nearest whole number

print(str(1) + " 1")

# requesting data:
user_input = input("Please enter youre name: ")
print("Hello "+ user_input+ "!")

# input only accepts strings, so we need to convert it to an int
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print("Result without changing type: " + num1 + num2)
print("Result with changing type: " + str(int(num1) + int(num2)))


# Exercises:
space_shuttle_name = "Determination"
shuttle_speed_mph = 17500
distance_to_mars = 225000000
distance_to_moon = 384400
miles_per_kilometer = 0.621

print(type(space_shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars))
print(type(distance_to_moon))
print(type(miles_per_kilometer))

miles_to_mars = distance_to_mars * miles_per_kilometer
hours_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hours_to_mars / 24
print(space_shuttle_name + " will take " + str(days_to_mars))


miles_to_moon = distance_to_moon * miles_per_kilometer * miles_per_kilometer
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print(space_shuttle_name + " will take " + str(days_to_moon))