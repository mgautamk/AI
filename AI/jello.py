from itertools import permutations
 
n = 8
#cols = range(n)
#for vec in permutations(cols):
    #if (n == len(set(vec[i]+i for i in cols))
    #== len(set(vec[i]-i for i in cols))):
        #print vec

def nQueenAlgo(n):
    modN = n % 12
    evn = []
    odd = []
    for i in range(1,n+1):
        if i%2 == 0:
            evn.append(i)
        else:
            odd.append(i)
    if modN == 3 or modN == 9:
        evn.remove(2)
        evn.append(2)
        odd.remove(1)
        odd.remove(3)
        odd.append(1)
        odd.append(3)
    if modN == 8:
        length = len(odd)
        if length % 2 != 0:
            length-=1
        for i in range(0,length,2):
            tmp = odd[i]
            odd[i] = odd[i+1]
            odd[i+1] = tmp
    if modN == 2:
        odd.remove(1)
        odd.insert(1,1)
        odd.remove(5)
        odd.append(5)
    total = evn+odd
    qList = []
    i = 0
    for queen in total:
        qList.append((queen-1,i))
        i+=1
    return qList

def main():
    nQueenAlgo(n)
