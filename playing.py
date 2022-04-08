art="Arturo"
#print(a)

def my_function():
    """Este es un texto de ayuda de como utilizar esta función  """
    pass

print(id(art))
art+=" Javier"
print(id(art))
art=art.upper()
print(id(art))
print(id("Arturo"))


def fibonacci(max):
    a, b = 0, 1
    while a <= max:
        yield a
        a, b = b, a+b


def primes(max):
    p = [2]

    j=2
    for i in p:
        if j % i == 0:
            #no es primo, pues es divisible entre un primo
            continue
        else:
            yield i
            p.append(i)



for i in primes(10):
    print(i)
