#1
x = int(input("Type a number: "))
while x>-1:
    print(x)
    x=x-1
#2
def print_and_return(list):
    print(list[0])
    return(list[1])
list=[5,7]
print(print_and_return(list))
#3
som=0
def first_plus_length(list1):
    som=list1[0]+list1[len(list1)-1]
    return(som)

list1=[1,2,3,4]
som=first_plus_length(list1)
print(som)
#4
def values_greater_than_second(arr):
    second=arr[1]
    li=[]
    b=0
    for i in range(2,len(arr)):
        if arr[i]>second :
            print(arr[i])
            break
    for i in range(0,len(arr)):
        if arr[i]>second :
            li.append(arr[i]) 
    if len(li)<2 :
        return("false")
    else :
        return li  

list2=[5,2,3]
print(values_greater_than_second(list2))

#5
def length_and_value(a,b):
    list=[]
    for i in range(0,a):
        list.append(b)
    return list


a=int(input("type a number "))
b=int(input("type a number "))
print(length_and_value(a,b))