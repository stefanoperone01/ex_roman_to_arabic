"""
Created on Wed Nov 30 15:18:26 2022

@author: stefanoperone01
"""
#roman = input('Roman: ')
def one_char(roman):
    if len(roman)==1:
        if roman=='I':
            roman = 1
        elif roman == 'V':
            roman = 5
        elif roman == 'X':
            roman = 10
        elif roman == 'L':
            roman = 50
        elif roman == 'C':
            roman = 100
        elif roman == 'D':
            roman = 500
        elif roman == 'M':
            roman = 1000
        elif roman == ' ':
            raise ValueError('Lo spazio è un carattere non concesso')
        else:
            raise ValueError('La lettera '+roman+' non corrisponde a un numero')
    return int(roman)

def convert_roman_to_arabic(roman: str) -> str:
    """
    convert a string containing a number in roman coding to a
    string containing the number in arabic (positinal) coding
    :param roman: string to be converted
    :return: converted string
    """
    
    if len(roman)==1:
        tot = str(one_char(roman))
        
    elif len(roman)>1:
        number = list(roman)
        temp = []
        tot = 0
        for i in range(len(number)):
            temp.append(one_char(number[i]))
            if i == 1:
                if temp[i-1]<temp[i]:
                    tot += temp[i]-temp[i-1]
                else:
                    tot += temp[i]+temp[i-1]   
            elif i > 1:
                if i > 2:
                    if temp[i]==temp[i-1]==temp[i-2]==temp[i-3]:
                        raise ValueError ('Numero romano non esistente')
                if temp[i-1]<temp[i] and temp[i-2]<temp[i]:
                    raise ValueError ('Numero romano non esistente')
                elif temp[i-1]<temp[i] and temp[i-2] > temp[i-1]:
                    tot += temp[i]-2*temp[i-1]
                elif temp[i-1]<temp[i]:
                    tot += temp[i]-temp[i-1]
                else:
                    tot += temp[i]
    return str(tot)
# tot = convert_roman_to_arabic(roman)
# print(tot)
                    
                