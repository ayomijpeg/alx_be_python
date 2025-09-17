# control-flow/daily_reminder.py

# Ask user for task details
task = input("Enter your task: ")

# Loop until a valid priority is given
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Please enter a valid priority: high, medium, or low.")

time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start building the reminder
reminder = ""

# Match case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# If statement for time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print final reminder
print("Reminder:", reminder)
