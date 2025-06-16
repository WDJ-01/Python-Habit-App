from storage import get_all_habits, get_completions
from datetime import datetime, timedelta

def list_habits():
    """
    returns a list of of habits

    Returns:
       list(object)

    """
    return list(map(lambda x: x[0], get_all_habits()))

def list_by_periodicity(periodicity):
    """
    returns a list of habits based of the entered periodicity

    Parameters:
      periodicity (string)
    
    Returns:
       list(object)
    
    """
    return list(filter(lambda x: x[1] == periodicity, get_all_habits()))

def get_longest_streak(habit_name):
    """
    returns a the numbre of the longest streak per habit

    Parameters:
      habit_name (string)
    
    Returns:
       streak value (int)
    
    """

    completions = sorted(get_completions(habit_name))
    if not completions:
        return 0

    habit = list(filter(lambda h: h[0] == habit_name, get_all_habits()))[0]
    period = timedelta(days=1) if habit[1] == "daily" else timedelta(days=7)

    streak = max_streak = 1
    for i in range(1, len(completions)):
        if completions[i] - completions[i - 1] <= period:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1
    return max_streak

def get_overall_longest_streak():
    """
    returns the habit with the longest streak
    
    Returns:
       name of habit (string)
       number of streak (int)

    """
    return max(map(lambda h: (h[0], get_longest_streak(h[0])), get_all_habits()), key=lambda x: x[1], default=("None", 0))
