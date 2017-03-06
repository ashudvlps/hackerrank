# You are given an immutable string, and you want to make changes to it.
# val = input()
values = list(input())
mutVal = input().split(" ")
values[int(mutVal[0])] = mutVal[1]
print("".join(values))
