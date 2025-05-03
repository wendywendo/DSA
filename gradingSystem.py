def show_history() -> None:
    print("\n Brief history of python")
    print("\n Created in the year 1991")
    print("\n py3 in the year 2008")

    print("\n** Program that computes average score of student ***")


def get_names_score() -> tuple[list[str], list[float]]:
    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Please enter a number greater than zero")

                continue

        except ValueError:
            print("Invalid input")
            continue

        names_of_students = []
        scores = []

        print("\n Enter student names and their scores: ")

        for i in range(count):
            name = input(f"Student { i + 1 } name: ").strip()
            if not name:
                name = f'Student: { i + 1 }'

            names_of_students.append(name)

            while True:
                try:
                    score = float(input(f"Enter the score for { name }:"))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100")

                except ValueError:
                    print("Invalid input")

        return names_of_students, scores 

def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def calculate_grade(grade: float):
    if grade >= 70:
        return "A"

    elif grade >= 60:
        return "B"

    elif grade >= 50:
        return "C"

    elif grade >= 40:
        return "D"

    elif grade >= 30:
        return "E"


result = get_names_score()

names = result[0]
scores = result[1]

for i in range(len(names)):
    print(f"{names[i]} has a score of {scores[i]}: Grade {calculate_grade(scores[i])}")

average = calculate_average(scores)
print(f"The average for the scores is { average }")
