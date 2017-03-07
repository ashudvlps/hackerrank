def capitalize(string):
    strings = string.split(" ")
    pString = []
    for v in strings:
        if len(v)>0:
            pString.append(v[0].upper()+v[1:])
        else:
            pString.append(v)
    return " ".join(pString)
