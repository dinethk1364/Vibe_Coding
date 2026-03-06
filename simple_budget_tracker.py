def main():
    try:
        # Ask the user for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        expenses = []
        # Ask for multiple expenses until 'done' is typed
        while True:
            user_input = input("Enter expense (or type 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            try:
                expense = float(user_input)
                expenses.append(expense)
            except ValueError:
                print("Error: Please enter a valid numeric value for the expense.")
        
        # Subtract expenses from total budget
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses
        
        # Displays remaining balance
        print(f"\nTotal Budget: LKR {total_budget:.2f}")
        print(f"Total Expenses: LKR {total_expenses:.2f}")
        print(f"Remaining Balance: LKR {remaining_balance:.2f}")
        
        if remaining_balance < 500:
            print("Warning: Low Funds")
        
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
