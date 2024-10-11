numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# заменить значение пропущенного элемента средним арифметическим

# Ищем индекс первого None элемента
index_of_none = numbers.index(None)
numbers[index_of_none] = 0
# Заменяем None средним арифметическим всех чисел
mean = sum(numbers) / len(numbers)
numbers[index_of_none] = mean

print("Измененный список:", numbers)
