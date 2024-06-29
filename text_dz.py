import re
# task 1 
print("Задание 1")
text_input = str(input("Введите текст: "))
words_input = str(input("Введите зарезервированные слова (буква тоже работает) через запятую: "))

# для правильной интерпритации слов программой, они разделяются через split(","), strip() убирает пробелы

words_input = [word.strip() for word in words_input.split(",")]


# программа ищет слова (параметр word) в words_input, если они совпадают со словами в тексте
founded_words = [word for word in words_input if word in text_input]

if founded_words:
    founded_words_upper = [word.upper() for word in words_input if word in text_input]
    print("Найденные слова: ", founded_words)
else:
    print("Введённое вами слово/а не найдены в тексте")

print("Задание 2")

text = str(input("Введите какой либо текст, разделяя предложния точками: "))
sentences = text.split(".")
number_of_sentences = len(sentences) - 1 #  - 1, потому что про программа считает так: [something].[something].[something].[empty string], количество элементов между точками
print(f"Количество предложений в введённом тексте соответствует числу: {number_of_sentences}")

# доп. задание
print("доп. задание")

text = input("Введите текст: ")


censured_words_input = input("Введите слова для цензурирования через запятую: ")

# Преобразуем строку слов для цензурирования в список 
censured_words = [word.strip() for word in censured_words_input.split(",")]

def censured(text, censured_words):
    #регулярное выражение для поиска слов, которые нужно удалить
    pattern = r'\b(' + '|'.join(re.escape(word) for word in censured_words) + r')\b'
    
    edited_text = re.sub(pattern, '', text)
    
    # лишние пробелы, которые могут остаться после удаления слов
    edited_text = re.sub(r'\s+', ' ', edited_text).strip()
    
   
    if edited_text != text:
        print("Результат:", edited_text)
    else:
        print("Слова для цензурирования не найдены в тексте")

censured(text, censured_words)

    
    # re.escape() - re module function. принимает строку, 
    # возвращая копию строки с экранированными символами
    # для интерпретации обычных символов в р.г. 
    # | -  логическое или 
    # r - raw string, для буквальной интепритации строк, без обработки экр. символов 
    #
    

# def censure(text, censured_words):
#     new_text = ""
#     for word in censured_words:
#         start_index = text.find(word)
#         end_index = start_index + len(word)

#         if text.find(word) != -1:
#             firs_section = text[:start_index]
#             second_section = text[end_index:]
#             new_text = firs_section + second_section

#     return new_text
