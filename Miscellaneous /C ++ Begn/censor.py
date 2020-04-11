def censor(text, word):
    
    str1=text.split()
    str2=[]
    
    for i in str1:
        if i == word:
            str2.append('*' *len(word))
        elif not i == str2:
            str2.append(i)
    return ' '.join(str2)
    
print(censor("this hack is wack hack","hack"))
