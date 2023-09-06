print('Printing the contents in the list in sorted form')
num = [2,5,10,4,50,36,51,49]
for i in sorted(num):
    print(i)

print('Printing the contents in the list in sorted form in REVERSE ORDER')
num = [2,5,10,4,50,36,51,49]
for i in sorted(num, reverse=True):
    print(i)


print('Sorting the names present in the list')
players = ['MS Dhoni','Virat Kohli','Rohit Sharma','Hardik Pandya']
for i in sorted(players, reverse=True):
    print(i)

print('For loop and dictionary')
d = {'f':1,'b':3,'a':9,'c':7}
for i in sorted(d.items()):
    print(i)

print('For loop and dictionary: Keys')
d = {'f':1,'b':3,'a':9,'c':7}
for i in sorted(d.keys()):
    print(i)

print('For loop and dictionary: Values')
d = {'f':1,'b':3,'a':9,'c':7}
for i in sorted(d.values()):
    print(i)


print('Reversing the names present in the list and printing with a for loop')
players = ['MS Dhoni','Virat Kohli','Rohit Sharma','Hardik Pandya']
for i in reversed(players):
    print(i)


print('Lamda function and for loop')
animals = [
    {'name':'Dog',
     'age':11},

{'name':'Cat',
     'age':4},

{'name':'Lion',
     'age':7},

{'name':'Cheethah',
     'age':8},

{'name':'Leopard',
     'age':15},
]

for animals in filter(lambda i: i['age']%2==0,animals):
    print(animals)

print('*************************')

print('WHILE LOOPS')

country = ['India','Canada','Brazil','Japan','Israel']
while country:
    print(country.pop(-1))

print('country: ',country)


print('*****************')

num = 10
while num>0: num = num -1; print(num)

# while True:
#     num = int(input('enter an interger: '))
#     print('The product of: ', num, "is", 5 * num)


print('*************************')
print('Enumerators')
for i in enumerate(['The','brown','fox','jumped','over','the','lazy','dog']):
    print(i)
    #Prints the results in the form of a tuple

print('*************************')
print('Enumerators: keys, values')
for key,value in enumerate(['The','brown','fox','jumped','over','the','lazy','dog']):
    print(key,value)
print('*************************')
print('Enumerators: keys, values')
for key,value in enumerate(['The','brown','fox','jumped','over','the','lazy','dog']):
    print(value,end=' ')
print('*************************')
print('/n')
company = 'mybigcompany'
#starts at index 3
for i,j in enumerate(company, start=3):
    print(i,j)

print('*************************')
print('Zip function')
first = ['Samay','Akash','Tanmay']
last = ['Raina','Gupta','Bhat']

for i in zip(first,last):
    print(i)



first = ['Samay','Akash','Tanmay']
last = ['Raina','Gupta','Bhat']
num=[1,2,3,4,5,6,7,8]

for i in zip(first,last,num):
    print(i)

print('*************************')
print('ITERTOOLS')
from itertools import zip_longest
first = ['Arjun','Ranveer','Alia']
last = ['Kapikad','Singh','Bhat']

for i in zip_longest(first,last):
    print(i)
print('*************************')

print('Fill value')
from itertools import zip_longest
first = ['Arjun','Ranveer','Alia','Bhuvanananan']
last = ['Kapikad','Singh','Bhat']

for i in zip_longest(first,last,fillvalue='LNU'):
    print(i)