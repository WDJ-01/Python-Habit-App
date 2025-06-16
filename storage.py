import sqlite3
from datetime import datetime

DB_NAME = "habits.db"

def init_db():
    """
    initializes the sqlite db by checking if the habits and completions table
    exist, if not then they are created

    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS habits (
                        name TEXT PRIMARY KEY,
                        periodicity TEXT,
                        created_at TEXT
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS completions (
                        habit_name TEXT,
                        completed_at TEXT,
                        FOREIGN KEY(habit_name) REFERENCES habits(name)
                    )''')
        conn.commit()

def add_habit(habit):
    """

    adds a habit to the habits table

    parameters:
      habit (Habit): the habit to add inhereting the Habit class
    
    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO habits VALUES (?, ?, ?)",
                  (habit.name, habit.periodicity, habit.created_at.strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()

def complete_task(habit_name):
    """
    
    adds a habit completion entry to completions table

    parameters:
      habit_name (str): the habit name
    
    """

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO completions VALUES (?, ?)",
                  (habit_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()

def get_all_habits():
    """
    
    returns a list of habits

    returns:
      list (Habit): all habits
    
    """

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT name, periodicity, created_at FROM habits")
        return c.fetchall()

def get_completions(habit_name):
    """
    
    returns a list of a habits completions

    parameter: 
      habit_name (string): habit name as a string value

    returns:
      list (dates): returns a list of dates
    
    """

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT completed_at FROM completions WHERE habit_name = ?", (habit_name,))
        return [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in c.fetchall()]

def delete_habit(habit_name):
    """
    
    removes a habit from the habit table and
    removes its completions from completions table

    parameters:
      habit_name (str): habit name as a string
    
    returns: 
      boolean: true or false if it was removed or not
    """

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM completions WHERE habit_name = ?", (habit_name,))
        c.execute("DELETE FROM habits WHERE name = ?", (habit_name,))
        conn.commit()
        return c.rowcount > 0 
