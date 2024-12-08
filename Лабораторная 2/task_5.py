# TODO  Напишите функцию count_letters

def count_letters(text):
# Словарь для подсчета букв
    letter_count = {}

    for char in text:
# Приводим символ к нижнему регистру
        lower_char = char.lower()
# Проверка - является ли символ буквой
        if lower_char.isalpha():
 # Увеличиваем счетчик для буквы
            if lower_char in letter_count:
                letter_count[lower_char] += 1
            else:
                letter_count[lower_char] = 1

    return letter_count

# TODO Напишите функцию calculate_frequency

def calculate_frequency(letter_count):

# Вычисление общего количества букв
    total_letters:int = sum(letter_count.values())

# Новый словарь для частот
    frequency_dict = {}

    for letter, count in letter_count.items():
# Вычисление частоты и округление до двух знаков после запятой
        frequency = format(count / total_letters, '.2f')
        frequency_dict[letter] = frequency

    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# Подсчитывание буквы
letter_counts = count_letters(main_str)

# Вычисление частоты
frequencies = calculate_frequency(letter_counts)

# TODO Распечатайте в столбик букву и её частоту в тексте

for letter, freq in frequencies.items():
    print(f"{letter}: {freq}")