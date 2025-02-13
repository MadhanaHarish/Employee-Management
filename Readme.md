\# Employee Management System

## Overview
The Employee Management System is a desktop application built using Python's Tkinter library for the GUI and SQLite for the database. This application allows users to manage employee records, including adding, updating, deleting, and searching for employee details.

## Features
- **Login Authentication**: Secure login mechanism for accessing the application.
- **Add Employee**: Input employee details and save them to the database.
- **Update Employee**: Modify existing employee records.
- **Delete Employee**: Remove employee records from the database.
- **Search Employee**: Search for employee records based on specific criteria.

## Installation
To run this project, ensure you have Python installed on your machine along with the Tkinter library. You can install any necessary dependencies using `pip`.

```bash
pip install tk
```

## How to Use
1. **Login**: Start the application and log in using the username "madhan" and password "admin@123".
2. **Main Window**: Once logged in, the main window will allow you to manage employee records.
    - **Add Employee**: Fill in the employee details and click "Add Details".
    - **Update Employee**: Select an employee record, modify the details, and click "Update Details".
    - **Delete Employee**: Select an employee record and click "Delete Details".
    - **Search Employee**: Use the search bar to find employee records by name or email.

## File Structure
- `main.py`: The main script that runs the application.
- `db.py`: Contains the `Database` class for interacting with the SQLite database.

## Future Enhancements
- Implementing more secure authentication mechanisms.
- Adding more search criteria for better employee management.
- Enhancing the UI for better user experience.

## Contact
For any queries or suggestions, feel free to reach out to me at myemail@example.com.
