def word_in_sentence_count(s):
    s_list=s.split()
    num = len(s_list)
    return num
def world_in_sentence_count_alt(s):
    s_list = s.split()
    return len(s_list)

#word_sentence_count(Lines, [0])

def word_in_file(infile):
    Lines=infile.readlines()
    
    word_count = 0
    for  line in Lines:
        word_count = word_count + word_in_sentence_count(line)

    return word_count
