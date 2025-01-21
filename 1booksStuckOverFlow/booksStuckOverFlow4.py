import string
foo = 1
bar = 'Bar'
baz = 3.14
# print(f'{0} - {1} - {2}'.format(foo,bar,baz))
# Создает строку в нижнем регистре
print(bar.casefold())
print(bar.lower())
# Создает строку в верхнем регис
print(bar.upper())
# Создает первую букву в верхем регистре
print(bar.capitalize())
print(bar.title())
# Замена регистров каждого символа строки
print(bar.swapcase())
# Map str
a = map(str.upper,["German", "Vova"])
print(list(a))
# Замена символов на другие символы
translatiom_table = str.maketrans("aeiou", "12345")
my_string = "This is a string"
asd = translated = my_string.translate(translatiom_table)
print(asd)
# Символы ascii
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
# Содержит все десятичные знаковые символы
print(string.digits)
# Содержит все шестнацатиричные символы
print(string.hexdigits)
# Содержит восьмеричные символы
print(string.octdigits)

# Удаление пробелов и символов
strA = ' тест на пробел '
print(strA.strip())
# Удаление сначала символов потом пробелов
strB = '<<< тест на символы <'
print(strB.strip('<').strip())
# Удаление с конца строки str.rstrip() и начала строки str.lstrip()
# Обратить порядок символов в строке
print(list(reversed(strA)))
strC = "This is a sentence"
asx = strC.split()
if len(asx) == 4:
    print(' Сплитовалось 4 блока '.strip())
strD = "Earth,Moon,Sun"
# Сплитование с запятыми создание списк
print(strD.split(','))
asz = strD.split(',')
print(type(asz))
# Замена в нутри строки слов букв цифр
strE = 'Привет меня зовут Влад'
print(strE.replace('Влад', 'Герман'))
# Проверка строк если все символы это буквы если есть пробел то будет False
print(strE.isalpha())
print('БезПробела'.isalpha())
# Проверка если регистр имеет тот или иной регистр
print('IS UPPER'.isupper())
asfg = 'Проверка регисра'
asg = asfg.upper()
if asg.isupper():
    print('Все символы в верхнем регистре')
# Объеденение строк в одну строку
print(" ".join(['once', 'upon', 'a', 'time']))
# Разделение строки дефисом
print("-".join(['once', 'upon', 'a', 'time']))

# Подсчет сколько раз символы встречаются в строке
print('German'.count('German'))

# Проверка с чего начинается строка
strF = 'German'
print(strF.startswith('Ge'))
# Проверка чем заканчивается строка
print(strF.endswith('n'))
# Кодировка Uncode
strG = b'\xc2\xa9abc'
print(strG.decode('utf-8'))
strH = 'kodirovanie'
print(strH.encode('utf-8'))