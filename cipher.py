print("Латиница")

text = input("Введите текст на латинице для шифровки: ")

if not text.isalpha():
    print("Ошибка: Введенный текст содержит цифры или символы.")
else:
    shift = 1
    
    def caesar(txt, shift):
        result = ""
        for char in txt:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    start = ord('a') # unicode symbol 
                else:
                    start = ord('A')
                result += chr(start + (ord(char) - start + shift_amount) % 26)
            else:
                result += char
        return result

   
    encryption = caesar(text, shift)
    print("С шифровкой: ", encryption)
    
    text2 = input("Введите текст на латинице для дешифровки: ")
    
    if not text2.isalpha():
        print("Ошибка: Введенный текст содержит цифры или символы.")
    else:
        decryption = caesar(text2, -shift)
        print("С дешифровкой: ", decryption)
    
    
print("Кириллица")



text = input("Введите текст на кириллице для шифровки: ")

if not text.isalpha():
    print("Ошибка: Введенный текст содержит цифры или символы.")
else:
    shift = 1
    
    def caesar(txt, shift):
        result = ""
        for char in txt:
            if char.isalpha():
                shift_amount = shift % 32
                if char.islower():
                    start = ord('а') # unicode symbol 
                else:
                    start = ord('А')
                result += chr(start + (ord(char) - start + shift_amount) % 32)
            else:
                result += char
        return result

   
    encryption = caesar(text, shift)
    print("С шифровкой: ", encryption)
    
    text2 = input("Введите текст на кириллице для дешифровки: ")
    
    if not text2.isalpha():
        print("Ошибка: Введенный текст содержит цифры или символы.")
    else:
        decryption = caesar(text2, -shift)
        print("С дешифровкой: ", decryption)


