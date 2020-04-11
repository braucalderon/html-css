def lower_case(let):
    num= ord(let)
    if num >= ord('a') and num <= ord('z'):
        return True
    else:
        return False
    
def encode_letter(word, key):
    num=ord(letter)
    new_num = num + key
    if lower_case(letter) and new_num > ord ('z'):
        new_num = new_num - 26
    if upper_case(letter) and new_num > ord('Z'):
        new_num = new_number - 26
    new_letter = chr(new_num)
    return new_letter


    

# def funct(letter, key)
#and retun letter shifted "key"
#steps forward
#chr(97)=a
#ord('c')=99
def encode_word(word, key):

    new_word= ""
    for l in word:
        new_l = encode_letter(l, key)
        new_word=new_word + new_l

    return new_word
        
def encode_file(plain, coded):
    Lines = plain.readlines()

    for line in Lines:
        line_list = line.split()
        for word in line_list:
            encode_word = encode_word(word,key)
            print (encoded_word, file = coded, end = " ")
    
