x = [ [5,2,3], [10,8,9] ] 
students1 = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1

print(x)
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        if x[i][j]==10:
            x[i][j]=15
print(x)

#1.2
print(students1)
for i in range(0,len(students1)):
    if students1[i]['last_name']=='Jordan':
        students1[i]['last_name']= 'Bryant'
print(students1)

#1.3
print(sports_directory)
for i in range(0,len(sports_directory['soccer'])):
    if sports_directory['soccer'][i]=='Messi':
        sports_directory['soccer'][i]='Andres'
print(sports_directory)

#1.4
print(z)
z[0]['y']=30
print(z)

#2=================================================================
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        print(f"first_name : {some_list[i]['first_name']}, last_name : {some_list[i]['last_name']}")

iterateDictionary(students)

#3=================================================================
def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)

#4=================================================================
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(len(dojo['locations']), 'LOCATIONS')
    for i in range(0,len(dojo['locations'])):
        print(dojo['locations'][i])
    print(len(dojo['instructors']), 'INSTRUCTORS')
    for i in range(0,len(dojo['instructors'])):
        print(dojo['instructors'][i])
printInfo(dojo)
