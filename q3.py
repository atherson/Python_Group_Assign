def get_grade(avg_mark):
    if avg_mark <= 59:
        return "Fail"
    elif avg_mark <= 66:
        return "D"
    elif avg_mark <= 76:
        return "C"
    elif avg_mark <= 86:
        return "B"
    else:
        return "A"

def main():
    while True:
        adm_no = int(input("What is your admission number?: "))
        surname = input("What is your surname?: ")

        total_marks = 0
        for subject in range(1, 4):
            mark = int(input(f"What is your mark for subject {subject}: "))
            print("The average mark should be less than or equal to 100!")
            total_marks += mark

                

        avg_mark = total_marks / 3
        grade = get_grade(avg_mark)

        print(f"\nStudent Admission Number: {adm_no}")
        print(f"Student Surname: {surname}")
        print(f"Average Mark: {avg_mark:.2f}")
        print(f"Grade: {grade}\n")

        continue_input = input("Do you want to compute for another student? (Y/N): ").strip().upper()
        if continue_input == 'N':
            print("Exiting the program.")
            break
        elif continue_input != 'Y':
            print("Invalid input, exiting the program.")
            break

if __name__ == "__main__":
    main()
