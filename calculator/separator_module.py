
def separator(input_string):
    temp = ''
    result=[]
    set_before_minus = {':','*','^',''}
    clean = []
    clean2 = []

    for i,symb in enumerate(input_string[:-1]):
        if symb == "+" or (symb == "-" and input_string[i-1] not in set_before_minus) :
            result.append(temp)
            temp =''
        temp += symb
    temp += input_string[-1]
    result.append(temp)

    for x in result:
        if any("i" in filt for filt in x) == True:
            clean.append(x)
        else:
            clean2.append(x)

    clean = ''.join(clean)
    if clean[0] == '+':
        clean = ''.join([clean[i] for i in range(len(clean)) if i != 0])      
    clean2 = ''.join(clean2)
    if clean2[0] == '+':
        clean2 = ''.join([clean2[i] for i in range(len(clean2)) if i != 0]) 

    return clean2, clean

