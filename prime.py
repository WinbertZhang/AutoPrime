def insertPrimes():
    fileObj = open('primes.txt', 'r')
    words = fileObj.read().splitlines()
    return set([int(n) for n in words])