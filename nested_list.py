if __name__ == '__main__':
    students = []  # Nested list to store students' names and grades

    # Input the number of students
    n = int(input())

    # Input each student's name and score
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    scores = sorted(set(student[1] for student in students))  # Unique sorted scores
    second_lowest_score = scores[1]

    # Find the names of students with the second lowest grade
    students_with_second_lowest = [student[0] for student in students if student[1] == second_lowest_score]

    # Sort the names alphabetically
    students_with_second_lowest.sort()

    # Print the names of students with the second lowest grade
    for student in students_with_second_lowest:
        print(student)
