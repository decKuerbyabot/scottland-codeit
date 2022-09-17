global left_letter
left_letter = []
letterdic={1:'A', 2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}


def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def quordleKeynoard_part1(answers, attempts):
    dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    ans = []
    left = ''
    for element in answers:
        for letter in element:
            ans.append(letter)
    for each in attempts:
        for key, value in dict.items():
            if (value != 0):
                dict[key] += 1
        if each in answers:
            answers.remove(each)
            for e in each:
                ans.remove(e)
        for e in each:
            if e not in ans:
                if dict[e] == 0:
                    dict[e] = 1
    res = ''
    for key, value in dict.items():
        if value != 0:
            res += str(value)
        else:
            left += key
    left_letter.append(left)
    return res

def quordleKeynoard_part2(answers, attempts, numbers):
    # it is weird that calling the function will change the output
    part1_ans = quordleKeynoard_part1(answers, attempts)
    print(part1_ans)
    res = ''
    num = []
    l=[]
    for i in range(len(numbers)):
        l.append(numbers[i])
        if ((i+1)%5 == 0):
            num.append(l)
            l=[]

    for character in num:
        for i in range(len(character)):
            if str(character[i]) in str(part1_ans):
                character[i] = "1"
            else:
                character[i] = "0"
        decn = binaryToDecimal(int("".join(character)))
        if decn >= 1 and decn <= 26:
            res += letterdic[decn]
    if (len(left_letter) != 0):
        left = left_letter[0]
        res += left
    return res
