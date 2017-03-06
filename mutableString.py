# You are given an immutable string, and you want to make changes to it.
val = input()
mutVal = input().split(" ")
values = []
for v in val:
    values.append(v)
values[int(mutVal[0])] = mutVal[1]
print("".join(values))
