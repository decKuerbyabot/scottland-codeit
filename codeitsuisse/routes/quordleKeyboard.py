left_letter = []
def quordleKeynoard_part1(answers, attempts, numbers):
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
            get = each
            answers.remove(get)
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
    part1_ans = quordleKeynoard_part1(answers, attempts, numbers)
    res = ''
    num = []
    l=[]
    for i in range(len(numbers)):
        l.append(numbers[i])
        if ((i+1)%5 == 0):
            num.append(l)
            l=[]
    for character in num:
        character_bin = ''
        for c in character:
            if str(c) in str(part1_ans):
                character_bin += '1'
            else:
                character_bin += '0'
        character_letter = int(character_bin, 2)
        res += chr(ord('@')+character_letter)
        character_bin = '' 
    left = left_letter[0]
    res += left
    return res 
