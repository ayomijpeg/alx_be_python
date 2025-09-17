# control-flow/daily_reminder.py

# Ask user for task details
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Enter priority (high/medium/low): ").lower()

# Start building the reminder message
reminder = f"Reminder: {task} [Priority: {priority}]"

# Add time-bound info
if time_bound == "yes":
    reminder += " - Immediate action required!"

# Customize based on priority using match-case
match priority:
    case "high":
        reminder += " ⚠️ High priority!"
    case "medium":
        reminder += " 🔔 Medium priority."
    case "low":
        reminder += " ✅ Low priority, no rush."

# Print the final reminder
print(reminder)
