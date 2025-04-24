import csv
from datetime import datetime, timedelta

FILENAME = "coding.csv"

def add_daily_log():
    topic = input("Enter topic (e.g., DSA, System Design): ").lower()
    language = input("Enter the language used: ").lower()
    try:
        duration = int(input("Enter duration in minutes: "))
    except ValueError:
        print("Invalid duration. Please enter a number.")
        return

    date = datetime.today().strftime("%Y-%m-%d")
    
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, topic, language, duration])
    
    print("Coding session logged successfully!")


def view_streak_and_average():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            logs = list(reader)
            if not logs:
                print("No coding logs found.")
                return

            dates = sorted(set(row[0] for row in logs))
            total_duration = sum(int(row[3]) for row in logs)
            unique_dates = set(dates)

            # Calculate streak
            today = datetime.today().date()
            streak = 0
            while today.strftime("%Y-%m-%d") in unique_dates:
                streak += 1
                today -= timedelta(days=1)

            avg_duration = total_duration / len(unique_dates)

            print(f"\nCurrent Streak: {streak} days")
            print(f" Average Daily Coding Time: {avg_duration:.2f} minutes")

    except FileNotFoundError:
        print("No logs found yet.")


def track_topics():
    topic_count = {}
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                topic = row[1]
                topic_count[topic] = topic_count.get(topic, 0) + 1

        print("\ Tracked Topics:")
        for topic, count in topic_count.items():
            print(f"{topic.title()}: {count} session(s)")
    except FileNotFoundError:
        print("No logs found yet.")

# Main menu
while True:
    print("\n--- Coding Tracker ---")
    print("1. Add Daily Log")
    print("2. View Streak & Average Coding Time")
    print("3. Track Topics")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_daily_log()
    elif choice == '2':
        view_streak_and_average()
    elif choice == '3':
        track_topics()
    elif choice == '4':
        print("Exiting... Happy Coding!")
        break
    else:
        print("Invalid choice. Please try again.")
