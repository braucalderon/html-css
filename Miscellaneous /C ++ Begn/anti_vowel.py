def anti_vowel(text):
    string=''
    vowels=['a','e','o','i','u','A', 'E', 'I', 'O', 'U']
    for i in text:
        if i not in vowels:
            string += i
    return string

print (anti_vowel('Hey look Words!'))

