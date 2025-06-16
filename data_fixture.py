from habit import Habit
from storage import add_habit, complete_task
from datetime import datetime, timedelta

def create_fixture_data():
    """
    creates 5 predefined habits and their related data on completions.
    Is intended for testing
    
    """
    habits = [
        Habit("Brush Teeth", "daily"),
        Habit("Workout", "daily"),
        Habit("Weekly Review", "weekly"),
        Habit("Read Book", "daily"),
        Habit("Call Family", "weekly")
    ]
    for h in habits:
        add_habit(h)

    now = datetime.now()
    for i in range(28):
        complete_task("Brush Teeth")
        if i % 2 == 0:
            complete_task("Workout")
        if i % 7 == 0:
            complete_task("Weekly Review")
            complete_task("Call Family")
