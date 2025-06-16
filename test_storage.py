import unittest
import os
import sqlite3
from datetime import datetime
from storage import init_db, add_habit, complete_task, get_all_habits, get_completions, delete_habit, DB_NAME
from habit import Habit

class TestStorage(unittest.TestCase):
    def setUp(self):
        """creates a new db for test"""
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)
        init_db()
        
    def tearDown(self):
        """cleans up db after test"""
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)

    def test_init_db(self):
        """Test that the database is properly initialized with tables"""
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in c.fetchall()]
            self.assertIn('habits', tables)
            self.assertIn('completions', tables)

    def test_add_habit(self):
        """Test adding a habit to the database"""
        habit = Habit("Test Habit", "daily")
        add_habit(habit)
        
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("SELECT name, periodicity FROM habits WHERE name = ?", (habit.name,))
            result = c.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], "Test Habit")
            self.assertEqual(result[1], "daily")

    def test_complete_task(self):
        """Test completing a task for a habit"""
        habit = Habit("Test Habit", "daily")
        add_habit(habit)
        
        complete_task(habit.name)
        
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("SELECT completed_at FROM completions WHERE habit_name = ?", (habit.name,))
            result = c.fetchone()
            self.assertIsNotNone(result)
            completion_time = datetime.strptime(result[0], "%Y-%m-%d %H:%M:%S")
            self.assertLess((datetime.now() - completion_time).total_seconds(), 5)

    def test_get_all_habits(self):
        """Test retrieving all habits"""
        habits = [
            Habit("Habit 1", "daily"),
            Habit("Habit 2", "weekly")
        ]
        for habit in habits:
            add_habit(habit)
        
        # Get all habits
        all_habits = get_all_habits()
        self.assertEqual(len(all_habits), 2)
        
        habit_names = [habit[0] for habit in all_habits]
        self.assertIn("Habit 1", habit_names)
        self.assertIn("Habit 2", habit_names)

    def test_get_completions(self):
        """Test retrieving completions for a habit"""
        habit = Habit("Test Habit", "daily")
        add_habit(habit)
        
        complete_task(habit.name)
        complete_task(habit.name)
        
        completions = get_completions(habit.name)
        self.assertEqual(len(completions), 2)
        
        for completion in completions:
            self.assertIsInstance(completion, datetime)

    def test_delete_habit(self):
        """Test deleting a habit and its completions"""
        habit = Habit("Test Habit", "daily")
        add_habit(habit)
        complete_task(habit.name)
        
        success = delete_habit(habit.name)
        self.assertTrue(success)
        
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("SELECT name FROM habits WHERE name = ?", (habit.name,))
            self.assertIsNone(c.fetchone())
            
            c.execute("SELECT completed_at FROM completions WHERE habit_name = ?", (habit.name,))
            self.assertIsNone(c.fetchone())

    def test_delete_nonexistent_habit(self):
        """Test deleting a habit that doesn't exist"""
        success = delete_habit("Nonexistent Habit")
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main() 