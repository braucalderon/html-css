ef lower_case(let):
    num= ord(let)
    if num >= ord('a') and num <= ord('z'):
        return True
    else:
        return False
    
def decode_letter(word, key):
    num=ord(letter)
    new_num = num - key
    if lower_case(letter) and new_num < ord ('a'):
        new_num = new_num + 26
    if upper_case(letter) and new_num < ord('A'):
        new_num = new_number + 26
    new_letter = chr(new_num)
    return new_letter


    

# def funct(letter, key)
#and retun letter shifted "key"
#steps forward
#chr(97)=a
#ord('c')=99
def decode_word(word, key):

    new_word= ""
    for 1 in word:
        new_1 = decode_letter(1, key)
        new_word=new_word + new_l

    return new_word
        
def decode_file(plain, coded):
    Lines = plain.readlines()

    for line in Lines:
        line_list = line.split()
        for word in line_list:
            decode_word = decode_word(word,key)
            print (encoded_word, file = coded, end = " ")
        print("\n", file = decode)
    

