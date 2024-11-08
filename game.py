import random
from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке


for count in counts:
    eagle_count = 0
    tails_count = 0

    for i in range(count):
        if  EAGLE == choice(coin):    #  подсчитать количество выпаданий орлов и решек
            eagle_count += 1
        else:
            tails_count += 1
    # разделить минимальное число среди орлов и решек на максимальное число и сохранить результат
    list_freq.append(min(eagle_count, tails_count)/max(eagle_count, tails_count))

print(list_freq)
