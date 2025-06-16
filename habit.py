from datetime import datetime

class Habit:
    """

    this habit class represents a habit with a name, how often it should
    and its created date

    """
    def __init__(self, name, periodicity, created_at=None):
        """

        this is the contructor and is initialized when the habit class is used
    
        """
        self.name = name
        self.periodicity = periodicity  # 'daily' or 'weekly'
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        """
        
        created a dictionary of a habit

        returns:
          habit (dictionary)
    
        """
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
