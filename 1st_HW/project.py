import sys

def printing():
    print("Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade")
    print("----------------------------------------------------------")
    return 0

def Average(mid, final):
    return float((mid+final)/2)

def sort_dict_average(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1][3], reverse=True)
    sorted_dict = {key: value for key, value in sorted_items}
    return sorted_dict

def Grade(num):
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'

def read_grades(filename):
    student_grades = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            student = int(parts[0])
            name = parts[1] + ' ' + parts[2]
            midterm = int(parts[3])
            final = int(parts[4])
            average = Average(midterm, final)
            grade = Grade(average)
            student_grades[student] = (name, midterm, final, average, grade)
    return student_grades

def show(students_grade):
    printing()
    sorted_students_grade = sort_dict_average(students_grade)
    for student, (name, mid, final, average, grade) in sorted_students_grade.items():
        print(f"{student}\t{name}\t{mid}\t{final}\t{average}\t{grade}")
    return 0

def search(id, students_grade):
    if id not in students_grade.keys():
        print("NO SUCH PERSON.", end='')
    else:
        printing()
        print(f"{id}\t", end='')
        for value in students_grade[id]:
            print(f"{value}\t", end='')
    print()
    return 0

def changescore(id, students_grade):
    if id not in students_grade.keys():
        print("NO SUCH PERSON.")
    else:
        print("Mid/Final?", end=' ')
        input_type = input().lower()
        if input_type not in ['mid', 'final']:
            print()
            return 0
        else:
            print("Input new score:", end=' ')
            new_score = int(input())
            if new_score >= 0 and new_score <= 100:
                printing()
                print(f"{id}\t", end='')
                for value in students_grade[id]:
                    print(f"{value}\t", end='')
                print()
                print(f"Score changed.")
                name, mid, final, average, grade = students_grade[id]
                if input_type == 'mid':
                    mid = new_score
                elif input_type == 'final':
                    final = new_score
                average = Average(mid, final)
                grade = Grade(average)
                students_grade[id] = (name, mid, final, average, grade)
                print(f"{id}\t", end='')
                for value in students_grade[id]:
                    print(f"{value}\t", end='')
                print()
    return 0

def add(id, students_grade):
    mid, final = -1, -1
    if id in students_grade.keys():
        print("ALREADY EXISTS.")
        return 0
    else:
        print("Name: ", end=' ')
        name = input()
        while(mid<0 or mid>100):
            print("Midterm Score:", end=' ')
            mid = int(input())
            if(0<=mid<=100): break
            print("Wrong Midterm Score.")
            print()
        while(final<0 or final>100):
            print("Final Score:", end=' ')
            final = int(input())
            if(0<=final<=100): break
            print("Wrong Final Score.")
            print()
        average = Average(mid, final)
        grade = Grade(average)
        students_grade[id] = (name, mid, final, average, grade)
        print("Student added.")
        return 0

def searchgrade(find_grade, students_grade):
    if find_grade not in ['A', 'B', 'C', 'D', 'F']:
        return 0
    else:
        if find_grade not in [item[-1] for item in students_grade.values()]:
            print("NO RESULTS.")
        else:
            printing()
            for id, (name, mid, final, average, grade) in students_grade.items():
                if grade == find_grade:
                    print(f"{id}\t", end='')
                    for value in students_grade[id]:
                        print(f"{value}\t", end='')
                    print()
        return 0

def REMOVE(id, students_grade):
    if id not in students_grade.keys():
        print("NO SUCH PERSON.")
    else:
        del students_grade[id]
        print("Student removed")
    return 0

def quit(answer, students_grade):
    while (answer != None):
        if answer == 'yes':
            print(f"File name:", end=' ')
            new_file = input()
            with open(new_file, 'w') as new_file:
                for student, (name, mid, final, average, grade) in students_grade.items():
                    new_file.write(f"{student}\t{name}\t{mid}\t{final}\n")
                    answer = None
        elif answer == 'no':
            answer = None
        else:
            print(f"Save data?[yes/no]", end=' ')
            answer = input().lower()
    return 0

def main():
    try:
        val = sys.argv[1]
    except:
        val = 'students.txt'
    students_grade = read_grades(val)
    print('#', end=' ')
    operation = input().lower()
    while(operation != 'quit'):
        if(operation == 'show'):
            show(students_grade)
            print()
        elif(operation == 'search'):
            print("Student ID:", end=' ')
            id = int(input())
            search(id, students_grade)
            print()
        elif(operation == 'changescore'):
            print("Student ID:", end=' ')
            id = int(input())
            changescore(id, students_grade)
            print()
        elif(operation == 'add'):
            print("Studnet ID:", end=' ')
            id = int(input())
            add(id, students_grade)
            print()
        elif(operation == "searchgrade"):
            print("Grade to search: ", end=' ')
            grade = input().upper()
            searchgrade(grade, students_grade)
            print()
        elif(operation == 'remove'):
            if not students_grade:
                print("List is empty.")
                print()
            else:
                print("Student ID:", end=' ')
                id = int(input())
                REMOVE(id, students_grade)
                print()
        print('#', end=' ')
        operation = input().lower()
    if(operation == 'quit'):
        print(f"Save data?[yes/no]", end=' ')
        answer = input().lower()
        quit(answer, students_grade)
    sys.exit()

if __name__ == "__main__":
    main()
