# structure: 
      # if condition_is_true:
         # Run this code
      # else:
         # Run this other code



# Python is case-sensitive, true and false are NOT valid boolean values.

# DATA TYPES: 


#  1. The string (str) data type represents a collection of       characters.

#  2. The integer (int) data type represents a whole number.

#  3. The float (float) data type represents a decimal value.

#  4. The boolean (bool) data type represents True or False.

name = 'Cynthia'
other_name = 'Rose'

print(name, other_name, name == other_name)

other_name = name 

print(name, other_name)

# operators: 

# Equal (==)
# Not equal (!=)
# Greater than (>)
# Less than (<)
# Greater than or equal (>=)
# Less than or equal (<=)
# in : 
#     Returns True if the left-hand value is found inside the           right-hand value
#     This operator does NOT work for the int or float data types
#     Ex: (True)
#         'a' in 'Happy'
#         'stop' in 'unstoppable'
#     Ex: (False)
#         'A' in 'apple' (case matters)
#         'oy' in 'you' (order matters)


#  logical operators: and, or, and not.

name = 'Bob' # Other names to try: 'Username', 'Rumpelstiltskin'

print(name)
print('Longer than 5 characters: ', len(name)>5)
print('Shorter than 10 characters: ', len(name)<10)
print('len(name) > 5 and len(name) < 10: ', len(name)>5 and len(name)<10)

print('a' in 'xyz' and len('flower') >= 6 or 5 + 5 == 10)

user_number = input("Enter number: ")
number = int(user_number)
if number %2 == 0:
  print("EVEN!")
  if number> 0:
    print("POSITIVE")
word = input('Please enter a word: ')
if len(word) == 4:
   print("What did your mom tell you about using 4-letter words?")
else:
   if len(word) < 4:
      print("You can think of a longer word than that!")
   else:
      print("Excellent word!")
# else if : elif
