import re
def is_isogram(string):
    patron = r'\w'
    result = re.findall(patron, string)
    string = ''.join(result)
    long = len(string)
    if long > 0:
        string = string.upper()
        for index in range(long-1):
            if string[index] in string[index+1::]:
                return False
    return True