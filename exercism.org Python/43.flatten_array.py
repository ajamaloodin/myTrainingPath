def flatten(iterable):
    tmp_list = " ".join(map(str,iterable))
    digits = []
    dig = ''
    flag = False
    how_many = len(tmp_list)
    for index, strs in enumerate(tmp_list):
        if strs in "0123456789-":
            flag = True
            dig = dig + strs
        else:
            if flag:
                digits.append(dig)
                dig = ''
                flag = False
        if index+1 == how_many and strs in "0123456789":
            digits.append(dig)
    result_list = []
    for item in digits:
        result_list.append(int(item))
    return result_list

