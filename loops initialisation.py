# Intialising for loops

name = ['akshay','gaurav','piyush','mayank']

for x in name:

    print(x)

#looping through a string

for x in 'akshay':

    print(x)

#demonstrating break in loops
for x in name:
    print(x)
    if x == "piyush":

      
      break
#demonstrating continue command in FOR loops
for x in name:
    print(x)
    if x == "piyush":
       continue

    #Inialising while loops in python
    i = 100
    while i < 150:
        print(i)
        if (i==130):
           break
        i+= 1

