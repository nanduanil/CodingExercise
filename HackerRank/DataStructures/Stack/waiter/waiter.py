def findPrime_SOE(upperLimit):
    primes = [2,3]
    primesToCheck = []
    possiblePrimes = {}
    if(upperLimit < 2): return []
    if(upperLimit == 2): return [2]
    if(upperLimit < 5): return primes
    
    for i in range(5,upperLimit+1,2):
        if(i%3 == 0):
            continue
        possiblePrimes[i] = True
        primesToCheck.append(i)
        
    for j in primesToCheck:
        if(possiblePrimes[j]):
            primes.append(j)
            for k in range(j*j,upperLimit,j):
                if(k in possiblePrimes):
                    possiblePrimes[k] = False
    return primes

command = [int(x) for x in input().strip().split()]
plateStack = []
for i in range(0,command[1]):
    try:
        plateStack.append([int(x) for x in input().strip().split()])
    except:
        plateStack.append([])

numberOfStack = len(plateStack)
plateStack.append([])
#as numberOfStack has upper limit of 1200 the highest prime we have
#to find is 1200th prime.
primes = findPrime_SOE(10000)
plateStackB = []
for j in range(0,numberOfStack):
    currentStack = plateStack[j]
    plateStackB.append([])
    while(len(currentStack)>0):
        item = currentStack.pop()
        if(item % primes[j] == 0):
            plateStackB[j].append(item)
        else:
            plateStack[j+1].append(item)


plateStackB.append(plateStack[-1])
for stack in plateStackB:
    while(len(stack)>0):
        print(stack.pop())