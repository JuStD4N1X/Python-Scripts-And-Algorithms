def filler(tab):
    for i in range(100):
        tab.append(True)

def eratosthenes(A):
    A[0]=False
    A[1]=False
    for i in range(2,10):
        if A[i]:
            for j in range(i*i,100,i):
                A[j]=False

    return A

if __name__ == '__main__':
    tab = []
    filler(tab)
    result = eratosthenes(tab)
    prime_numbers = [i for i in range(100) if result[i]==True]
    print(prime_numbers)

