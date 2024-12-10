für i in bereich(1, 20):
    wenn i % 5 == 0 und i % 3 == 0:
        ausgeben('FizzBuzz')
    sonst_wenn i % 3 == 0:
        ausgeben('Fizz')
    sonst_wenn i % 5 == 0:
        ausgeben('Buzz')
    sonst:
        ausgeben(i)
