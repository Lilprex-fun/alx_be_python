# Daily Reminder Task Manager
# This script uses match case to manage task reminders based on priority and time sensitivity

# Prompt user for task input
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ")

# Ask if task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Process task based on priority using match case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Schedule time to complete it soon.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Try to complete it this week.")
    
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("Invalid priority level. Please choose from high, medium, or low.")
