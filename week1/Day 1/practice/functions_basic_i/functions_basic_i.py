#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #display 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() , number_of_military_branches()) #error


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #display 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #display 5


#5
def number_of_great_lakes():
    print(5)     #display 5
x = number_of_great_lakes()
print(x) #display the return of function (5)


#6
def add(b,c):  
    print(b+c)   #display 3 / display 5 /display 8
print(add(1,2) + add(2,3)) #display 8


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #display 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b) #display 100
    if b < 10: #false
        return 5
    else:
        return 10 
    return 7
print(number_of_oceans_or_fingers_or_continents()) #display 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #display 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #display 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #display 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #display 8


#11
b = 500
print(b) #display 500
def foobar():
    b = 300
    print(b) #display 300
print(b) #display 500
foobar() 
print(b) #display 500


#12
b = 500
print(b) #display 500
def foobar():
    b = 300
    print(b) #display 300
    return b
print(b) #display 500
foobar() 
print(b) #display 500


#13
b = 500
print(b) #display 500
def foobar():
    b = 300
    print(b) #display 300
    return b
print(b) #display 500
b=foobar() 
print(b) #display 300


#14
def foo():
    print(1) #display 1
    bar() 
    print(2) #display 2
def bar():
    print(3) #display 3
foo() 


#15
def foo():
    print(1) #display 1
    x = bar()
    print(x) #display 5
    return 10
def bar():
    print(3) #display 3
    return 5
y = foo() 
print(y) #display 10