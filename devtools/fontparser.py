with open('devtools/fa.js') as f:
    content = f.readlines()
content = [x.strip() for x in content]

icons = []
parsed_icons = []
banned_chars = [
'{', '}', '(', ')', ';'
]

def hasNoBannedChars(x):
    for char in banned_chars:
        if char in x: return False
        else: return True

for line in content:
    line = line.split('": [')[0]
    if line.startswith('"'):
        line = line.replace('"', '')
        if hasNoBannedChars(line):
            icons.append(line)

icons.sort()
for icon in icons:
    if not icon in parsed_icons:
        parsed_icons.append(icon)

for icon in parsed_icons:
    icon = '{"text": "fa-' + icon + '","sidetext": "Font Awesome"},'
    print(icon)
