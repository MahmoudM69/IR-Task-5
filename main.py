from numpy.lib.scimath import sqrt
from math import floor

p1 = [2, 4, 8, 16, 19, 23, 28, 41, 43]
p2 = [1, 2, 3, 5, 8, 41, 51, 60, 71]
answer = []


def skippointer(l1, l2):
    l2idx = 0
    l1idx = 0
    sqrl1 = floor(sqrt(len(l1)))
    sqrl2 = floor(sqrt(len(l2)))
    while(l2idx < len(l2) and l1idx < len(l1)):
        if(l2[l2idx] == l1[l1idx]):
            answer.append(l2[l2idx])
            l2idx += 1
            l1idx += 1
        elif(l2[l2idx] < l1[l1idx]):
            if(((l2idx + sqrl2) < len(l2)) and (l2[l2idx + sqrl2] < l1[l1idx])):
                while(((l2idx + sqrl2) < len(l2)) and (l2[l2idx + sqrl2] < l1[l1idx])):
                    l2idx += sqrl2
            else:
                l2idx += 1
        else:
            if(((l1idx + sqrl1) < len(l1)) and (l1[l1idx + sqrl1] < l2[l2idx])):
                while(((l1idx + sqrl1) < len(l1)) and (l1[l1idx + sqrl1] < l2[l2idx])):
                    l1idx += sqrl2
            else:
                l1idx += 1
    print(answer)


skippointer(p1, p2)
