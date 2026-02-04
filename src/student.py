def calculate_average(marks):
    """Calculates the mean of a list of marks."""
    if not marks:
        return 0
    return sum(marks) / len(marks)

def get_grade(average):
    """Determines the grade based on the average score."""
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"

def main():
    print("--- Student Grade Calculator ---")

    marks = []
    for i in range(1, 6):
        score = float(input(f"Enter marks for subject {i}: "))
        marks.append(score)
        
    avg = calculate_average(marks)
    grade = get_grade(avg)
        
    print(f"\nAverage Marks: {avg:.2f}")
    print(f"Final Grade: {grade}")
  

if __name__ == "__main__":
    main()