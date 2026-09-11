def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    result =a
    return result

if __name__ == '__main__':
    a = int(input("Podaj a "))
    b = int(input("Podaj b "))

    result = gcd(a,b)
    print(f"Wynik to {result}")