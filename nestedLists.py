# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
# Constraints
# 2<=N<=5
# There will always be one or more students having the second lowest grade.
if __name__ == '__main__':
    students = []
    scores = []
    outList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name,score])
    listScore = list(set(scores))
    listScore.sort()
    outScore = listScore[1]
    for i in students:
        if i[1]==outScore:
            outList.append(i[0])
    outList.sort()
    for val in outList:
        print(val)
