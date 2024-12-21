def main ():
    n = input()
    words = input().split()
    text = words[0]
    words.pop(0)
    for word in words:
        text_len = len(text)
        word_len = len(word)
        for index in range(min(word_len, text_len)):
            if word.startswith(text[text_len - word_len + index +1:]) and text[text_len - word_len + index +1:] != "":
                break
        text = text[:text_len - word_len + index +1]   
        text = text + word 

    print(text)            

main()    