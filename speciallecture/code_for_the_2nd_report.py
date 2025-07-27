# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。

def calc_total_and_avg(grades):
    total = sum(grades)
    avg = total / len(grades)
    return total, avg

def run(students):
    top_total = -1
    top_name = ""
    for name, grades in students.items():
        total, avg = calc_total_and_avg(grades)
        if total > top_total:
            top_total = total
            top_name = name
        print(f"Student: {name}, Total: {total}, Average: {avg}")
    return top_name, top_total

students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 85, 90]
}

top_student, top_score = run(students)
print(f"Best student: {top_student} with total score: {top_score}")
