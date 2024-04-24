
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