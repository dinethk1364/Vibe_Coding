def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'exit':
        print("Exiting program...")
        return None
    return user_input

def main():
    print("--- Student Grade Calculator ---")
    print("Type 'Exit' at any prompt to quit.\n")
    
    while True:
        # Ask for student's name
        name = get_input("Enter student's name: ")
        if name is None: break

        # Ask for 3 subject marks
        try:
            m1_raw = get_input("Enter mark for Subject 1: ")
            if m1_raw is None: break
            mark1 = float(m1_raw)

            m2_raw = get_input("Enter mark for Subject 2: ")
            if m2_raw is None: break
            mark2 = float(m2_raw)

            m3_raw = get_input("Enter mark for Subject 3: ")
            if m3_raw is None: break
            mark3 = float(m3_raw)
            
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

            # Print formatted output
            print("-" * 30)
            print(f"Name : {name}")
            print(f"Average: {average:.1f}")
            print(f"Grade : {grade}")
            print("-" * 30)
                
        except ValueError:
            print("Invalid input. Please enter numerical marks or 'Exit'.")

if __name__ == "__main__":
    main()
