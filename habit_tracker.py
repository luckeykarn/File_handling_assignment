import json
import os
from datetime import datetime

habit_file = "habits.json"

# Load existing habits
if os.path.exists(habit_file):
    with open(habit_file, "r") as file:
        habits = json.load(file)
else:
    habits = []

while True:
    print("\n--- Habit Tracker ---")
    print("1. Add Habit")
    print("2. Mark Habit as Done")
    print("3. View Habit Streaks")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter habit name: ").lower()
        frequency = input("Enter frequency (daily/weekly): ").lower()
        date = input("Date (YYYY-MM-DD) or press Enter for today: ")
        if date == "":
            date = datetime.now()
            date = date.strftime("%Y-%m-%d")
        print(date)
        
        habit = {
            "name": name,
            "frequency": "daily",
            "dates":date
        }
        print(habit)
        habits.append(habit)
        with open(habit_file, "w") as file:
            json.dump(habits, file, indent=4)
        print(f"Habit '{name}' added successfully!")

    elif choice == "2":
        name = input("Enter the habit name to mark as done: ").lower()
        today = datetime.now().strftime("%Y-%m-%d")

        found = False
        for habit in habits:
            if habit["name"] == name and habit["frequency"] == "daily":
                # Check if the habit is already marked for today
                habit[frequency] = "daily"
                found = True
                break

        if found:    
                    with open(habit_file, "w") as file:
                        json.dump(habits, file, indent=4)
                    print(f"Habit'{name}' marked as done for today.")
        else:
                    print(f"Habit '{name}' not found or not a daily habit.")
                    found = True
                    break
        if not found:
            print("Habit not found.")

    elif choice == "3":
        print("\n--- Habit Streaks ---")
        habit_list = []
        for habit in habits:
            streak_count = 0
            habit_list.append(habit['name'])
            
            # if habit["frequency"] == "daily" or habit["frequency"] == "weekly":
            #     # Calculate streak count
            #     streak_count = len(habit["dates"])
            #     print(f"Habit: {habit['name']}, Streak: {streak_count} days")
            #     break
        # print("my habbit list :",list(set(habit_list)))
        habit_list = list(set(habit_list))
        streak_data = {}
        for my_habit in habit_list:
            streak = 0 #re-assign streak.
            for habit in habits:
                if my_habit == habit['name']:
                    streak = streak + 1,
                    # print(my_habit,"equal ::",streak)
                    # input("pause")
            streak_data[my_habit] = streak
        
        print(streak_data," streak data")
            
    elif choice == "4":
        print("Thank you for using the Habit Tracker!")
        break

    else:
        print("Invalid option. Please try again.")



