import unittest
from habit import Habit

class TestHabit(unittest.TestCase):
    """
    Test for Habit class

    test the creation fo the habit class a varyfies its values
    
    """
    
    def test_creation(self):
        """
        Test a habit can be created with name and period 
        and timestamp is automatically generated if not given
        
        """
        h = Habit("Test Habit", "daily")
        self.assertEqual(h.name, "Test Habit")
        self.assertEqual(h.periodicity, "daily")
        self.assertIsNotNone(h.created_at)

if __name__ == '__main__':
    unittest.main()
