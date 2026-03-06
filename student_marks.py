def get_valid_mark(subject_num):
    while True:
        try:
            mark = float(input(f"Enter mark for Subject {subject_num}: "))
            if -1 < mark < 101:
                return mark
            else:
                print("Invalid input. Mark must be between -1 and 101.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    while True:
        # Ask for student's name
        name = input("\nEnter student's name (or type 'Exit' to quit): ")
        
        # Check if user wants to exit
        if name.strip().lower() == 'exit':
            print("Exiting program.")
            break

        # Ask for 3 subject marks with validation
        mark1 = get_valid_mark(1)
        mark2 = get_valid_mark(2)
        mark3 = get_valid_mark(3)

        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3

        # Determine Grade
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Display result
        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")
        print(f"Grade  : {grade}")
        print("-" * 30)

if __name__ == "__main__":
    main()
