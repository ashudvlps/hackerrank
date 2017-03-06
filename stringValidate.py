inString = input()
isaln = False
isalp = False
isdig = False
islow = False
isupp = False
for v in inString:
    if v.isalnum():
        isaln = True
    if v.isalpha():
        isalp = True
    if v.isdigit():
        isdig = True
    if v.islower():
        islow = True
    if v.isupper():
        isupp = True
print(isaln)
print(isalp)
print(isdig)
print(islow)
print(isupp)
