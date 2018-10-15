FORMAT = True #add json around the class
x = [] #the two lists we use to store the css classes
a = []
BANNED = [ #helps remove anything that isn't a class
'>',',',':','(',')',' ','[',']', '+'
]

with open('devtools/bulma.min.css', 'r') as f: #open the file
    file = f.readlines()

CSS = str(file).replace('}', '{').split('{') #split the file

def subsplit(x, s): #this removes anything if it follows a BANNED simbol
    z = []
    for i in x:
        y = i.split(s)
        for i in y:
            if i.startswith('.'):
                z.append(i)
    return z

for item in CSS: #split the classes
    if item.startswith('.'):
        for i in item.split('.'):
            y = f'.{i}'
            if y != '.':
                a.append(y)

for i in BANNED: #remove anything that isn't a class
    a = subsplit(a, i)

x = [] #reset the first list to be re-used
for i in a: #remove duplicates
    if not FORMAT: #keep the dot, append to list
        if not i in x:
            x.append(i.replace('~', ''))
    else: #remove the dot, append to list
        if not i.replace('.', '') in x:
            x.append(i.replace('.', '').replace('~', ''))

x.sort() #sort the classes

if FORMAT:
    for i in x:
        i = '{"text": "' + i + '","sidetext": "Bulma"},'
        print(i)
else:
    for i in x:
        print(i)
