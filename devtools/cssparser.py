import os

dot = False #keep the dot at the start of the class
format = True #add json around the class
x = [] #the two lists we use to store the css classes
a = []
banned = [ #helps remove anything that isn't a class
'>',',',':','(',')',' ','[',']', '+', '~'
]

fileo = open('devtools/bulma.css', 'r') #open the file
file = fileo.readlines()
fileo.close()
css = str(file).replace('}', '{').split('{') #split the file

def subsplit(x, s): #this removes anything if it follows a banned simbol
    z = []
    for i in x:
        y = i.split(s)
        for i in y:
            if i.startswith('.'):
                z.append(i)
    return z

for item in css: #split the classes
    if item.startswith('.'):
        for i in item.split('.'):
            y = f'.{i}'
            if y != '.':
                a.append(y)

for i in banned: #remove anything that isn't a class
    a = subsplit(a, i)

x = [] #reset the first list to be re-used
for i in a: #remove duplicates
    if dot: #keep the dot, append to list
        if not i in x:
            x.append(i)
    else: #remove the dot, append to list
        if not i.replace('.', '') in x:
            x.append(i.replace('.', ''))

x.sort() #sort the classes

if format:
    for i in x:
        i = '{"text": "' + i + '","sidetext": "Bulma"},'
        print(i)
else:
    for i in x:
        print(i)
