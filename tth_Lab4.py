
# Lab 4A - Fibonacci Sequence

def fibonacci(num):
    fibonacci = []

    for i in range(num):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2])

    return fibonacci[len(fibonacci) - 1]


# Lab 4B - Prime Numbers

def is_prime(num):
    isPrime = True

    if num == 1:
        isPrime = False

    if num < 0:
        isPrime = False

    for i in range(num - 1, 2, -1):
        if num%i == 0:
            isPrime = False

    return isPrime


# Lab 4C - Prime Factorization

def print_prime_factors(number):
    factorList = []
    i = 2
    num = number

    while i <= number:
        if num%i == 0:
            num/=i
            factorList.append(i)
        else:
            i += 1

    if len(factorList) == 0:
        factorList.append(number)

    print(f"{number} = ",end='')
    print(*factorList, sep=" * ")