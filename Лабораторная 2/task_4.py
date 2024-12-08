# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
# Разделение строки на списки участников
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

# Пересечение двух множеств
    common_participants = participants1.intersection(participants2)

# Возвращаем отсортированный список общих участников
    return sorted(common_participants)

# Использование функции с заданными строками и разделителем '|'

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common_participants)

# Проверка работы функции с разделителем запятая
participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

common_participants_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma)
print("Общие участники (с запятой):", common_participants_comma)

# TODO Провеьте работу функции с разделителем отличным от запятой
