num1 = 42 # variable integer declaration
num2 = 2.3 # variable float declaration
boolean = True # variable boolean declaration
string = 'Hello World' # variable string declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Data Types tuples initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Data Types dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') # Data Types list initialize 
print(type(fruit)) # type check
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # Tuples add value
print(person['name']) # log statement
person['name'] = 'George' # Dictionary add value
person['eye_color'] = 'blue' # Dictionary add value
print(fruit[2]) #log statement

if num1 > 45: #conditional if
    print("It's greater") # log statement
else: #conditional else
    print("It's lower") # log statement

if len(string) < 5: #conditional if
    print("It's a short word!") # log statement
elif len(string) > 15: #conditional else if
    print("It's a long word!") # log statement
else:  #conditional else
    print("Just right!") # log statement

for x in range(5): #for loop start
    print(x) #log statement
for x in range(2,5): #for loop start
    print(x) #log statement
for x in range(2,10,3): #for loop start
    print(x) #log statement
x = 0        # variable declaration
while(x < 5): #while loop start
    print(x) #log statement
    x += 1   #while loop increment

pizza_toppings.pop() # Tuples delete value
pizza_toppings.pop(1) # Tuples delete value

print(person) #log statement
person.pop('eye_color') # Dictionary delete value
print(person)  #log statement

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': #conditional if
        continue   # for loop continue
    print('After 1st if statement')  #log statement
    if topping == 'Olives':  #conditional if
        break # for loop break

def print_hello_ten_times(): # function parameter
    for num in range(10):  # for loop start
        print('Hello')  #log statement

print_hello_ten_times() # function argument

def print_hello_x_times(x): # function parameter
    for num in range(x): # for loop start
        print('Hello') #log statement

print_hello_x_times(4) # function argument

def print_hello_x_or_ten_times(x = 10): # function parameter
    for num in range(x): # for loop start
        print('Hello') #log statement

print_hello_x_or_ten_times() # function argument
print_hello_x_or_ten_times(4) # function argument


"""
Bonus section #comment multiline
"""

# print(num3) #comment single line
# num3 = 72 #comment single line
# fruit[0] = 'cranberry' #comment single line
# print(person['favorite_team']) #comment single line
# print(pizza_toppings[7]) #comment single line
#   print(boolean) #comment single line
# fruit.append('raspberry') #comment single line
# fruit.pop(1) #comment single line