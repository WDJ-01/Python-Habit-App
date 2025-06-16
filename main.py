from storage import init_db, add_habit, complete_task, delete_habit
from analytics import *
from data_fixture import create_fixture_data
from habit import Habit

def menu():
    """

    created a menu in the terminal allowing user to select an action

    """
    print("\n=== Habit Tracker CLI ===")
    print("1. Add Habit")
    print("2. Complete Habit")
    print("3. List All Habits")
    print("4. Habits by Periodicity")
    print("5. Longest Streak (Per Habit)")
    print("6. Longest Streak Overall")
    print("7. Load Fixture Data")
    print("8. Delete Habit")
    print("9. Exit")

def run():
    """

    This method acts as an entry point fo the program. It runs when
    python3 main.py is called. Initializing the sqlite db and providing
    prompts to the user. The correct functions are then executed based of 
    the prompt.
    
    """
    init_db() #initializes sqlite db
    while True:
        menu() #creates menu in terminal
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Enter habit name: ")
            period = input("Enter periodicity (daily/weekly): ").lower()
            add_habit(Habit(name, period))
        elif choice == "2":
            name = input("Habit name to complete: ")
            complete_task(name)
        elif choice == "3":
            print(list_habits())
        elif choice == "4":
            p = input("Enter periodicity to filter: ").lower()
            print(list_by_periodicity(p))
        elif choice == "5":
            name = input("Enter habit name: ")
            print(f"{name} longest streak: {get_longest_streak(name)}")
        elif choice == "6":
            name, streak = get_overall_longest_streak()
            print(f"Longest streak: {name} with {streak} periods")
        elif choice == "7":
            create_fixture_data()
            print("Fixture data loaded.")
        elif choice == "8":
            name = input("Enter habit name to delete: ")
            if delete_habit(name):
                print(f"Habit '{name}' has been deleted successfully.")
            else:
                print(f"Habit '{name}' not found.")
        elif choice == "9":
            break

if __name__ == "__main__":
    run()
