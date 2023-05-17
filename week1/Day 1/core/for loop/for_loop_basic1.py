#Print all integers from 0 to 150
for i in range(0,151):
    print(i)

#Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001):
    if i%5==0 :
        print(i)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for i in range(1,101):
    if i%10==0 and i%5==0 :
        print("Coding Dojo")
    elif  i%5==0 and i%10 != 0:
        print("Coding")
    else :
        print(i)

#Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for i in range(0,500000):
    if i%2!=0 :
        sum+=i

print("sum of odd integers from 0 to 500000 is",sum)

#Print positive numbers starting at 2018, counting down by fours.
sumpos=0
i=2018
while i>-1 :    
        sumpos=sumpos+i
        i-=4

print("sum of positive number from 2018 to 0 counting down by 4 is",sumpos)

#lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult

arr=""
LowNum=25
HighNum=50
mult=5
for i in range(LowNum,HighNum+1):
     if i%mult==0 :
          arr=arr+str(i)+","
arr=arr[:-1]
print("the number multiple mult is", arr)