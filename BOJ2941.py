def countAlphabet(word,N):
    global counter
    if change_alphabet2 in word:
        word = word.replace(change_alphabet2,"1")

    for char in change_alphabet1:
        if char in word:
            word = word.replace(char,"1")

    print(len(word))


word = str(input())
N = len(word)

change_alphabet1=['c=','c-','d-','lj','nj','s=','z=']
change_alphabet2 = 'dz='
countAlphabet(word,N)