def daily_steps_tracker():
    print("Welcome to the Daily Steps Tracker!")
    print("Enter the number of steps taken each day in the month, separated by spaces:")

    try:
        steps = list(map(int, input().split()))

        if not steps:
            print("No data provided. Please enter the number of steps for each day.")
            return
        
        highest_steps = max(steps)
        lowest_steps = min(steps)
        average_steps = sum(steps) / len(steps)
        sorted_steps_desc = sorted(steps, reverse=True)

        print(f"\nHighest steps in a day: {highest_steps}")
        print(f"Lowest steps in a day: {lowest_steps}")
        print(f"Average daily steps: {average_steps:.2f}")
        print(f"Step counts sorted in descending order: {sorted_steps_desc}")

    except ValueError:
        print("Invalid input! Please enter only numeric values separated by spaces.")


if __name__ == "__main__":
    daily_steps_tracker()       