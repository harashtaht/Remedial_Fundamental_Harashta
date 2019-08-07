#Soal 1 : Panjang dari Kata Terpendek di Kalimat

s1 = "Many people get up early in the morning"
s2 = "Every office would getting newest monitor"
s3 = "Create new file after this morning"

def find_short(s):
    lowerS = s.lower()
    splitS = lowerS.split(' ')
    list_len = []

    for i in splitS:
        list_len.append(len(i))
    LenKal = list(zip(list_len, splitS))

    for loop1 in range(0, len(LenKal)):
        for loop2 in range(loop1+1, len(LenKal)):
            if(LenKal[loop1][0] > LenKal[loop2][0]):
                LenKal[loop1], LenKal[loop2] = LenKal[loop2], LenKal[loop1]
    return len(LenKal[0][1])

print(find_short(s1))
print(find_short(s2))
print(find_short(s3))


########## ########## ######### ########## ########## #########
#SOAL 2 : Persistence 

def persistence(x):
    total_global = x
    step = 0
    while (total_global>=10):
        z = total_global
        y = str(z)
        total = 1
        for a in range (len(y)):
            total *= int(y[a])
        step += 1
        total_global = total
    return print(step)

persistence(39)
persistence(999)
persistence(4)

########## ########## ######### ########## ########## #########
# SOAL 3 : Multiplication Table


def multiplication_table(row, col):
    z = ''
    for zig in range(1, row+1):
        initial = 0
        loopnum = zig
        for zag in range(1, col+1):
            initial += loopnum
            z += str(initial)
            z += ' '
        z += '\n'
    return print(z)

multiplication_table(3,3)
multiplication_table(5,3)
multiplication_table(3,5)

# multiplication_table(4,6)
# multiplication_table(3,4)
# multiplication_table(9,2)


########## ########## ######### ########## ########## #########
# SOAL 4 : Alphabet Position & Dictionary

def alphabet_position(text):
    dict_alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 
    'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
    'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 
    'w': 23, 'x': 24, 'y': 25, 'z': 26}
    splitText = text.split()
    z = ''
    for word in splitText:
        for letter in word.lower():
            if letter in dict_alphabet:
                z += str(dict_alphabet[letter])
                z += ' '
            else:
                pass
    return print(z)

alphabet_position("The sunset sets at twelve o'clock")
alphabet_position("it's never too late to try")
alphabet_position("Have you done your homework?")
alphabet_position("Zzzzz Zzzzz I bought a xylophone in my sleep")
# text = input("Enter text: ")
# alphabet_position(text)

########## ########## ######### ########## ########## #########
# #SOAL 5 (BONUS): Prime Number

def is_prime(num):
    primeList = [2]
    numBeta = 3
    while primeList[-1] < num:
        for p in primeList:
            if numBeta % p == 0:
                break
        else:
            primeList.append(numBeta)
        numBeta += 2
    if primeList[-1] == num:
        return True
    else:
        return False 

# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(-1))   
# print(is_prime(5099))
# print(is_prime(5100))
# print(is_prime(6200))
# print(is_prime(5101))