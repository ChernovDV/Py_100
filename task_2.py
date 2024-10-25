# Напишите функцию find_common_participants
def find_common_participants(first, second, separator=','):
    first = first.split(separator)
    second = second.split(separator)
    third = set(first)
    third = list(third.intersection(second))

    return sorted(third)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,"|"))

