# formatting text homework 
def text_formatting():
    import string
    print("Enter text")
    user_input = str(input())  
    print("Before capitalization: ", user_input)
    def capitilize():
        sentences = string.capwords(user_input).split(". ")
        for sentence in sentences:
            result = ". ".join(sentence.capitalize())
        print("After capitalization: ", result)
    
    def char_find(text, character):
        char_counter = 0
        for char in text:
            char = "!" and "?" and "!?"
            char_counter = char_find(user_input, char)
            print(f"Character '{char}' is seen in the text {char_counter} times")

if __name__ == "__main__":
    text_formatting()
    
