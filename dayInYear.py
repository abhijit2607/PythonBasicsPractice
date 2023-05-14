def day_of_year():
    # Get the day number from the user
    day_num = int(input("Enter the day number (2-365): "))

    # Get the first day of the year from the user
    first_day = input("Enter the first day of the year (Mon/Tue/Wed/Thu/Fri/Sat/Sun): ")

    # Create a list of days of the week
    days_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    # Calculate the day of the week for the given day number
    day_of_week_num = (days_of_week.index(first_day.lower()) + (day_num - 1)) % 7

    # Display the day on the given day number
    print("Day " + str(day_num) + " is a " + days_of_week[day_of_week_num])

# Call the function
day_of_year()
