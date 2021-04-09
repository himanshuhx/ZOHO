#POON PLEE SAME POIE PLEA PLIE POIN
#TOON
#PLEA
from collections import deque
def getCount(start, target, dict):
    if start==target:
        return 0
    if target not in dict:
        return 0
    lvl, wrdLen = 0, len(start)
    queue = deque()
    queue.append(start)
    while queue:
        lvl+=1
        for i in range(len(queue)):
            word = [k for k in queue.popleft()]
            for j in range(wrdLen):
                org_char = word[j]
                for c in range(ord('a'),ord('z')+1):
                    word[j]=chr(c)
                    if("".join(word)==target):
                        return lvl+1
                    if(''.join(word) not in dict):
                        continue
                    queue.append("".join(word))
                word[j] = org_char
        return 0


dictionary = {"POON":1,"PLEE":1,"SAME":1,"POIE":1,"PLEA":1,"PLIE":1,"POIN":1}
start = input()
target = input()
print(getCount(start, target, dictionary))