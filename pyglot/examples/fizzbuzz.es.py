para i en rango(20):
    si i % 3 == 0 and i % 5 == 0:
      imprimir("fizzbuzz")
    sino_si i % 3 == 0:
      imprimir("fizz")
    sino_si i % 5 == 0:
      imprimir("buzz")
    sino:
      imprimir(i)