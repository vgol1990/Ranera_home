# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

print("---------Пункт А------------")
def remove_exclamation_marks():
    s = input("Введите предложение")
    text = s.replace('!', '')
    print(text)
remove_exclamation_marks()



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
print("---------Пункт B ------------")
def remove_last_em(s):
    if s[-1] == '!':
        s = s[:len(s) -1]
    return s
print(remove_last_em('Hi!'))
print (remove_last_em('Hi!!!'))
print (remove_last_em('!Hi'))

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


print("---------Пункт C------------")
def remove_word_with_one_em(s):
    sentence = ''
    words = s.split()
    for word in words:
        if '!' not in word or word.count('!') != 1:
            sentence += word + ' '
    return sentence.strip()

print(remove_word_with_one_em("Hi!"))
print(remove_word_with_one_em("Hi! Hi!"))
print(remove_word_with_one_em("Hi! Hi! Hi!"))
print(remove_word_with_one_em("Hi Hi! Hi!"))
print(remove_word_with_one_em("Hi! !Hi Hi!"))
print(remove_word_with_one_em("Hi! Hi!! Hi!"))
print(remove_word_with_one_em("Hi! !Hi! Hi!"))

