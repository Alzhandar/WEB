n = int(input())
students = []

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

unique_scores = sorted(set([score for name, score in students]))
second_highest_score = unique_scores[1]
second_highest_students = [name for name, score in students if score == second_highest_score]

for name in sorted(second_highest_students):
    print(name)
