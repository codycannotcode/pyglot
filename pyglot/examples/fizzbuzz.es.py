para i en rango(1, 20):
    si i % 5 == 0 y i % 3 == 0:
        imprimir('FizzBuzz')
    sino_si i % 3 == 0:
        imprimir('Fizz')
    sino_si i % 5 == 0:
        imprimir('Buzz')
    sino:
        imprimir(i)
