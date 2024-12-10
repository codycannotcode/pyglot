pour i dans intervalle(1, 20):
    si i % 5 == 0 et i % 3 == 0:
        imprimer('FizzBuzz')
    si_sinon i % 3 == 0:
        imprimer('Fizz')
    si_sinon i % 5 == 0:
        imprimer('Buzz')
    sinon:
        imprimer(i)
