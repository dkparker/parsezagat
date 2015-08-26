import platform
import re

with open("Zagat-NYC-2010.txt", 'r') as f:
    text = f.read()

lines = text.split('\r')
lines = filter(None, lines)

for i in range(len(lines)):
    lines[i] = ' '.join(lines[i].split())
    
lines = filter(None, lines)

for i in range(len(lines)):
    try:
        if lines[i][-1] in ".\"":
            lines[i] += '*'
    except IndexError:
        print len(lines[i])
        print lines[i]
        continue
    if "\"" in lines[i]:
        lines[i]+= '*'

for i, line in enumerate(lines):
    try:
        if line[-1] == '*' and lines[i+1][-1] == '*':
            for i in range(2):
                if line.endswith('*'):
                    line = line[:-1]
            line += lines[i+1]
            line = ' '.join(line.split())
            lines[i] = line
            lines.pop(i+1)
    except IndexError:
        continue

with open("newerText", 'w') as f:
    for line in lines:
        f.write(line + '\n')


