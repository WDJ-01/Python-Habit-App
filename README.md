# Python Habit App

Python habit tracking app used to help maintain healthy habit. The following document shows you how to clone the repository, run the app locally, create a executable for the app and an overview of the features.

## Features

- Create, delete and complete daily and weekly habits
- View and track completed habits
- View habit streaks both per habit and overall
- Save habits in SQLite database
- instructions for creating an executable for easy access

## Contents

- analytics.py
  contains all the functions related to streaks

- data-fixture.py
  contains code for creating predefined habits

- habit.py
  contains code for the Habit class used throughout the app

- main.py
  main netry point of the application. Is responsible for creating the options in the terminal and selecting the appropriate methods based of user input

- main.spec
  used as a configuration file for creating executable

- requirements.txt
  contains all required libraries and is used with pip install

- storage.py
  contains the methods for managing the habits and completions in the sqlite db

- test_habit.py
  unit test for the Habit class

- test_storage.py
  unit test for all sqlite methods regarding storage

## Installation

### Requirements

- Python 3.8 >
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd python-habit-app
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

- the app can be run from the terminal

```bash 
# Run directly with Python locally on device in terminal
python main.py

# Or use the executable, after running executable commands -> see Building Executables
./dist/main  # On macOS
dist/main.exe  # On Windows
```

### Basic Commands

- Create a habit
- Complete habit
- View all habits
- View analytics on habits
- Delete a habit

## Building Executables

### macOS

```bash
# Install PyInstaller if not already installed
pip install pyinstaller

# Create executable
pyinstaller --onefile main.py
```

The executable will be created in the `dist` directory.

### Windows

```bash
# Install PyInstaller if not already installed
pip install pyinstaller

# Create executable
pyinstaller --onefile main.py
```

The executable will be created in the `dist` directory as `main.exe`.

## Project Structure

```
python-habit-app/
├── main.py           # Main application entry point
├── habit.py          # Habit class definition
├── storage.py        # Database operations
├── analytics.py      # Statistics and analysis
├── test_habit.py     # Unit tests for Habit class
├── test_storage.py   # Unit tests for storage operations
└── requirements.txt  # Project dependencies
```

## Testing

Run the test suite using:

```bash
python -m unittest discover
```

## Acknowledgments

- Built with Python
- Uses SQLite for data persistence
- PyInstaller for creating executables
# python-habit-app
