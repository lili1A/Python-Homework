#formatting 
string = "Hello World\tHello"
print(string.center(20, "*")) #20 - numbres of whitespace/ any other symbols
print()
# замена таб на пробел. tabsize - макс. колво пробелов
print(string.expandtabs(tabsize=4))
print(len(string))
print(len(string.expandtabs(tabsize=4)))

# выравнивание по одному из краев  
string2 = "Python - cool"
print(string2.ljust(20, '$' )) # left 
print(string2.rjust(20, "@")) # right 
# удаление лишних символов
string3 = "     Hello   - World -----"
print(string3.rstrip("-"))
print(string3.lstrip())

# Срез строки
string = "0123456789"
print(string[0])
print(string[0:]) # срез с  по -1 индексы
print(string[5:])
print(string[5:-2]) # срез с  по -2 индексы

# to inverse string 
print(string[-1::-1]) # vice versa

print(string[0:-1:2])
print(string[0:-2:3])


""" Задание 1 Есть некоторый текст. 
Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы; 
■ Посчитайте сколько раз цифры встречаются в тексте; 
■ Посчитайте сколько раз знаки препинания встречаются в тексте; 
■ Посчитайте количество восклицательных знаков в тексте.

 """
 
 
""" 
import string - это стандартный модуль Python, который предоставляет набор констант и функций для работы со строками. 
В модуле string содержатся различные константы, такие как string.ascii_letters (строка, содержащая все буквы ASCII), 
string.digits (строка, содержащая все цифры), string.punctuation (строка, содержащая все знаки пунктуации), 
а также функции для работы со строками, такие как string.capwords() (капитализация первых букв каждого слова в строке) и другие.

Импортирование модуля string дает доступ к этим константам и функциям, что делает удобной работу со строками, особенно когда требуется манипулировать буквами, цифрами или знаками пунктуации.
 """
 
def txt():
    import string

    s = "python is cool  however, it is sometimes complicated. But i wont give up! i have 34 flowers and ny sister has 56, but our mom has 0!!!!"
    print("Исходная строка:")
    print(s)

    #  с помощью string.capwords() строка разбивается на предложения 
    sentences = string.capwords(s).split(". ")

    # Капитализируем только первую букву каждого предложения
    result = ". ".join(sentence.capitalize() for sentence in sentences)

    print("После капитализации первой буквы в предложениях:")
    print(result)


    def count_characters(text, char):
        count = 0
        for ch in text:
            if ch == char:
                count += 1
        return count

    char = "!"
    exclamation_count = count_characters(s, char)
    print(f"Символ '{char}' встречается {exclamation_count} раз(а) в тексте")

if __name__ == "__main__": # The if __name__ == "__main__": statement checks if the script is being run as the main program
    txt()


import string 
s = "This is the first sentence. This is the second sentence. And this is the third sentence."
# separating string by '.'\
sentences = string.capwords(s).split(". ")
print(sentences)

