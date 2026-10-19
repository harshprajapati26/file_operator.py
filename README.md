# File Operator – Personal Journal Manager

## 📌 Project Overview

**File Operator** is a beginner-friendly Python project that allows users to maintain a personal journal using text-file handling. Users can add new journal entries, view all saved entries, search for a specific keyword or date, and delete all entries when needed.

The project demonstrates basic **Object-Oriented Programming (OOP)**, file handling, exception handling, and a menu-driven user interface.

## 🎯 Objectives

- Learn how to read, write, append, and manage text files in Python.
- Understand file-opening modes such as `r`, `w`, `a`, and `x`.
- Practice input/output operations with text files.
- Use exception handling for errors such as `FileNotFoundError` and `PermissionError`.
- Apply OOP concepts by creating a class and its methods.
- Build a simple, menu-driven application.

## ✨ Features

1. **Add a New Entry** – Enter a journal note and save it to the file. The file is created automatically if it does not exist.
2. **View All Entries** – Display all saved journal entries, including their timestamps.
3. **Search for an Entry** – Find entries that contain a particular keyword or date.
4. **Delete All Entries** – Clear the journal after asking for confirmation.
5. **Exit** – Close the program safely.
6. **Error Handling** – Show understandable messages if the journal file is missing, access is denied, or an invalid menu option is entered.

## 🧠 Concepts Used

- Python classes and objects
- Instance methods
- Text-file handling
- File modes: `r`, `w`, `a`, and `x`
- `with open(...)` for working with files
- Exception handling with `try` and `except`
- User input and conditional statements
- Loops and menu-driven programming
- Timestamps using Python's `datetime` module

## 🛠️ Requirements

- Python 3
- Any Python editor, such as IDLE, VS Code, or PyCharm

No external libraries are required if the program uses Python's standard library.

## ▶️ How to Run

1. Download or clone this repository.
2. Keep the Python program and any required files in the same project folder.
3. Open the program in Python IDLE or another Python editor.
4. Run the Python file.
5. Choose an option from the menu and follow the on-screen instructions.

The journal file (`journal.txt`) will be created automatically when the program saves its first entry, if the code is written to create it when needed.

## 🖥️ Example Menu

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

### Example: Add a New Entry

```text
Enter your journal entry:
Today was a productive day. I learned about file handling in Python.

Entry added successfully!
```

### Example: View All Entries

```text
Your Journal Entries:
--------------------------------
[2024-12-25 10:00:00]
Today was a productive day. I learned about file handling in Python.
```

### Example: Search for an Entry

```text
Enter a keyword or date to search: productive

Matching Entries:
--------------------------------
[2024-12-25 10:00:00]
Today was a productive day. I learned about file handling in Python.
```

### Example: Delete All Entries

```text
Are you sure you want to delete all entries? (yes/no): yes

All journal entries have been deleted.
```

*The output examples are illustrative. The exact wording and timestamps may differ depending on your implementation.*

## 📁 Project Structure

```text
File-Operator/
├── README.md
└── FileOperator.py
```

The journal text file is created when the program needs it, so it may not appear in the repository at first.

## 🔮 Possible Future Improvements

- Add an option to edit an existing journal entry.
- Add categories or tags for journal notes.
- Export journal entries to another text file.
- Add a password-protection feature.
- Improve search to support case-insensitive matching.

## 👨‍💻 Author

**Name:** Your Name

## 📄 License

This project is created for educational and learning purposes.
