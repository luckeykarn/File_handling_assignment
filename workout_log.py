import json
import os
from datetime import datetime, timedelta

filename = "workouts.json"
workouts = []

# Load workouts if file exists
if os.path.exists(filename):
    with open(filename, "r") as f:
        workouts = json.load(f)

# Save to JSON
def save_workouts():
    with open(filename, "w") as f:
        json.dump(workouts, f, indent=4)

# Add workout
def log_workout():
    workout_type = input("Workout type: ")
    duration = int(input("Duration in minutes: "))
    date_input = input("Date (YYYY-MM-DD) or press Enter for today: ")

    if date_input == "":
        date_input = datetime.now().strftime("%Y-%m-%d")

    workout = {
        "type": workout_type,
        "duration": duration,
        "date": date_input
    }

    workouts.append(workout)
    save_workouts()
    print("Workout logged!")

# List all
def list_workouts():
    print("\n--- All Workouts ---")
    if len(workouts) == 0:
        print("No workouts found.")
    else:
        for workout in workouts:
            print(workout["date"], "|", workout["type"], "|", workout["duration"], "min")


# Total today
def total_today():
    today = datetime.now().date()
    total = 0
    for w in workouts:
        w_date = datetime.strptime(w['date'], "%Y-%m-%d").date()
        if w_date == today:
            total += w['duration']
    print(f"Today's workout total: {total} min")

# Total this week
def total_week():
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    total = 0
    for w in workouts:
        w_date = datetime.strptime(w['date'], "%Y-%m-%d").date()
        if w_date >= start_of_week:
            total += w['duration']
    print(f"This week's workout total: {total} min")

while True:
    print("\nCommands: add_log | show_list | today_workout | weekly_workout | exit")
    command = input("Enter command: ").lower()

    if command == "add_log":
        log_workout()

    elif command == "show_list":
        list_workouts()

    elif command == "today_workout":
        total_today()

    elif command == "weekly_workout":
        total_week()

    elif command == "exit":
        print("Thank you for using the workout log!")
        break

    else:
        print("Invalid command.")
