def gcd(x, y):
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            ans = i
    return ans


#######################################################################

def better_gcd(x, y):
    i = min(x, y)
    while i > 0:
        if (x % i == 0) and (y % i == 0):
            return i
        else:
            i = i - 1
    return


#######################################################################

# Function that returns all the factors of a given number

def factors(n: int):
    factorList = []
    for i in range(1, n + 1):
        if n % i == 0:
            factorList = factorList + [i]
    return factorList


#######################################################################

# function to check weather prime or not

def isPrime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#######################################################################

# function to print all the prime numbers in the list

def primeList(n: int):
    prime_list = []
    for i in range(1, n):
        if isPrime(i):
            prime_list = prime_list + [i]
    return prime_list


#######################################################################


# ans = better_gcd(int(input("Enter a number: ")), int(input("Enter another number: ")))
#
# print(ans)

# print(factors(int(input("Enter a number: "))))

# print(isPrime(int(input("Enter a number: "))))

# print(primeList(int(input("Enter a number: "))))
