для i в диапазон(1, 20):
    если i % 5 == 0 и i % 3 == 0:
        вывести('FizzBuzz')
    иначе_если i % 3 == 0:
        вывести('Fizz')
    иначе_если i % 5 == 0:
        вывести('Buzz')
    иначе:
        вывести(i)
